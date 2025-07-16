#!/usr/bin/env python3

import sys
import json
import datetime
import argparse
import ffmpeg
from colorama import Fore
from colorama import Style

from audio.audio_util import *
from helper.config import Config
from helper.logger import *
from helper import logger

CONFIG_PATH = '../conf/config.yml'


''' open and filter the audio
'''
def open_sound(config):
    # convert if necessary
    if config.input_audio_file_type not in ['.wav']:
        debug(f"converting [{config.input_audio_file}] to [.wav]")
        old_input_audio_file = config.input_audio_file
        new_input_audio_file = f"{config.audio_data_dir}/{config.input_audio_file_base_name}.wav"

        try:
            stream = ffmpeg.input(old_input_audio_file)
            # stream = ffmpeg.hflip(stream)
            stream = ffmpeg.output(stream, new_input_audio_file)
            ffmpeg.run(stream)

            config.input_audio_file = new_input_audio_file
            debug(f"converted  [{old_input_audio_file}] to [{config.input_audio_file}]")

        except Exception as e:
            error(str(e))
            exit(-1)


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
            print(segment_spec)
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
    for i, segment in enumerate(segments):
        if segment.content == 'voiced':
            info(f"{Fore.GREEN}.. {i:>3}. {segment}{Style.RESET_ALL}")
        else:
            info(f"{Fore.RED}.. {i:>3}. {segment}{Style.RESET_ALL}")

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
    with open(config.asr_output_file, "a", encoding="utf-8") as f:
        for i, segment in enumerate(segments):
            if segment.asr_response:
                # print(segment.asr_response)
                f.write(segment.to_string())
                f.write('\n')
                f.write(f"audio    : {segment.file}, asr time {segment.asr_response['processingTime']:3.2f}s, ratio {(segment.duration_ms/1000)/segment.asr_response['processingTime']:3.2f}")
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
    print(config)
    logger.LOG_LEVEL = config.log_level
    config.configure(file_name=args["audio"], range_spec=args["range"], segment_spec=args["segments"])

    sound = open_sound(config=config)

    segments = generate_segments(config=config, sound=sound)

    process_segments(config=config, segments=segments)

    write_output(config=config, segments=segments)
