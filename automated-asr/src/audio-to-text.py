#!/usr/bin/env python3

import sys
import json
import yaml
import datetime
import argparse
from pathlib import Path
from colorama import Fore
from colorama import Style

from audio.audio_util import *
from helper.logger import *

CONFIG_PATH = '../conf/config.yml'


''' do the segmentation manually
'''
def segment_manually(config):
    # open as sound
    sound = open_as_sound(config)
    info('original sound file info')
    info('--------------------------')
    print(printable_info(sound, config['input-audio-file']))


    # filter sound
    sound = filter(sound, config)
    info('filtered sound file info')
    info('--------------------------')
    print(printable_info(sound, config['input-audio-file']))



    if len(config['segments']) == 0:
        print(f"{Fore.YELLOW}.. no segments defined")
        return []

    # generate the segments
    segments = []
    for segment_spec in config['segments']:
        this_segment_start = segment_spec[0] * 1000
        this_segment_end = segment_spec[1] * 1000
        if this_segment_start > this_segment_end:
            info(f"segment start {this_segment_start} is greater than segment end {this_segment_end}")
        else:
            segment = Segment(start_ms=this_segment_start, end_ms=this_segment_end, content='voiced')
            segments.append(segment)

    return sound, segments



''' do the automatic segmentation
'''
def segment_automatically(config):

    # open as sound
    sound = open_as_sound(config)
    info('original sound file info')
    info('--------------------------')
    print(printable_info(sound, config['input-audio-file']))


    # filter sound
    sound = filter(sound, config)
    info('filtered sound file info')
    info('--------------------------')
    print(printable_info(sound, config['input-audio-file']))


    # identify silent segments
    segments = identify_segments(sound, config)
    info(f".. {len(segments)} segments found")

    return sound, segments



''' process the segments
'''
def process_segments(sound, segments, config):
    i = 0
    for segment in segments:
        if segment.content == 'voiced':
            info(f"{Fore.GREEN}.. {i:>3}. {segment.content} - [{(segment.start_ms/1000):6.2f} : {(segment.end_ms/1000):6.2f}]  -  duration : {(segment.duration_ms/1000):6.2f}{Style.RESET_ALL}")
        else:
            info(f"{Fore.RED}.. {i:>3}. {segment.content} - [{(segment.start_ms/1000):6.2f} : {(segment.end_ms/1000):6.2f}]  -  duration : {(segment.duration_ms/1000):6.2f}{Style.RESET_ALL}")

        i = i + 1

    print()


    # split by segments
    audio_files = split_segments(sound, segments, config)


    # do the asr
    do_asr_on_files(audio_files)

    return audio_files



''' write output
'''
def write_output(config, segments):
    # write output
    with open(config['asr-output-file'], "w", encoding="utf-8") as f:
        for segment in segments:
            if segment.asr_response:
                f.write(f"audio    : {segment.file}")
                f.write('\n')

                f.write(f"duration : {segment.duration_ms/1000:3.2f}s, asr time {segment.asr_response['processingTime']:3.2f}s, ratio {(segment.duration_ms/1000)/segment.asr_response['processingTime']:3.2f}")
                f.write('\n')

                f.write(segment.asr_response['text'])
                f.write('\n\n')



''' configure environment
'''
def configure(file_name, segments):
    config_path = Path(CONFIG_PATH).resolve()
    config = yaml.load(open(config_path, 'r', encoding='utf-8'), Loader=yaml.FullLoader)
    output_dir = config['output-dir']
    config['audio-data-dir'] = f"{output_dir}/audio"
    config['audio-out-dir'] = f"{config['audio-data-dir']}/splits"

    config['input-audio-file'] = f"{config['audio-data-dir']}/{file_name}.wav"
    config['output-file-format'] = f"{config['audio-out-dir']}/{file_name}-"

    config['asr-output-file'] = f"{config['output-dir']}/{config['asr-output-file']}"

    if segments:
        segment_list = []
        pairs = segments.split(' ')
        if len(pairs) > 1:
            for pair in pairs[1:]:
                splitted = pair.split(':')
                if len(splitted) == 2:
                    try:
                        segment_start = float(splitted[0])
                    except:
                        print(f"can not convert {splitted[0]} to anumber")
                        continue

                    try:
                        segment_end = float(splitted[1])
                    except:
                        print(f"can not convert {splitted[1]} to anumber")
                        continue
                
                    segment_list.append([segment_start, segment_end])

                else:
                    print(f"can not determine range from : {pair}")
                    continue

        if len(segment_list):
            config['segments'] = sorted(segment_list)

    return config



if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-a", "--audio", required=True, help="audio file name to process, without extension, wav assumed")
    ap.add_argument("-s", "--segments", required=False, help="list of segments (start_seconds:end_seconds) where audio is to be splitted manually, must be quoted")
    args = vars(ap.parse_args())

    config = configure(args["audio"], args["segments"])
    
    if 'segments' in config:
        sound, segments = segment_manually(config)
    else:
        sound, segments = segment_automatically(config)

    segments = process_segments(sound, segments, config)

    write_output(config, segments)