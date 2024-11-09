#!/usr/bin/env python3

import sys
import json
import datetime
import argparse
from colorama import Fore
from colorama import Style

from audio.audio_util import *
from helper.config import Config
from helper.logger import *

CONFIG_PATH = '../conf/config.yml'


''' open and filter the audio
'''
def open_sound(config):
    # open as sound
    sound = open_as_sound(config)

    # filter sound
    sound = filter(config, sound)

    return sound



''' do the segmentation
'''
def generate_segments(config, sound):
    # segment as specified
    if config.segments:
        if len(config.segments) == 0:
            print(f"{Fore.YELLOW}.. no segments defined")
            return []

        # generate the segments
        segments = []
        for segment_spec in config.segments:
            this_segment_start = segment_spec[0] * 1000
            this_segment_end = segment_spec[1] * 1000
            if this_segment_start > this_segment_end:
                warn(f"segment start {this_segment_start} is greater than segment end {this_segment_end}")
            else:
                segment = Segment(sound=sound, config=config, start_ms=this_segment_start, end_ms=this_segment_end, content='voiced')
                segments.append(segment)

    # programmatic segmentation
    else:
        # create the root segment and optimize
        sound_segment = Segment.from_sound(sound, config)
        sound_segment.break_down()
        segments = sound_segment.get_broken_down_segments()

        # merge segments for optmization
        segments = merge_segments(config=config, segments=segments)


    info(f".. {len(segments)} segments found")

    return segments



''' process the segments
'''
def process_segments(config, segments):
    i = 0
    for segment in segments:
        if segment.content == 'voiced':
            info(f"{Fore.GREEN}.. {i:>3}. {segment}{Style.RESET_ALL}")
        else:
            info(f"{Fore.RED}.. {i:>3}. {segment}{Style.RESET_ALL}")

        i = i + 1

    print()


    # split by segments
    split_segments(segments)


    # do the asr
    if config.do_asr:
        do_asr_on_files(segments)



''' write output
'''
def write_output(config, segments):
    # write output
    with open(config.asr_output_file, "w", encoding="utf-8") as f:
        for segment in segments:
            if segment.asr_response:
                print(segment.asr_response)
                f.write(f"audio    : {segment.file}")
                f.write('\n')

                f.write(f"duration : {segment.duration_ms/1000:3.2f}s, asr time {segment.asr_response['processingTime']:3.2f}s, ratio {(segment.duration_ms/1000)/segment.asr_response['processingTime']:3.2f}")
                f.write('\n')

                f.write(segment.asr_response['text'])
                f.write('\n\n')



if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-a", "--audio", required=True, help="audio file name to process, without extension, wav assumed")
    ap.add_argument("-r", "--range", required=False, help="audio range in sss.ms:sss.ms format to be processed")
    ap.add_argument("-s", "--segments", required=False, help="list of segments (start_seconds:end_seconds) where audio is to be splitted manually, must be quoted")
    args = vars(ap.parse_args())

    config = Config(CONFIG_PATH)
    config.configure(file_name=args["audio"], range_spec=args["range"], segment_spec=args["segments"])

    sound = open_sound(config=config)

    segments = generate_segments(config=config, sound=sound)

    process_segments(config=config, segments=segments)

    write_output(config=config, segments=segments)
