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

CONFIG_PATH = '../conf/config.yml'


''' do the processing
'''
def process_manually(config):
    # open as sound
    sound = open_as_sound(config)
    print(printable_info(sound, config['input-audio-file']))

    if len(config['segments']) == 0:
        print(f"{Fore.YELLOW}.. no segments defined")
        return []

    # generate the segments
    segments = []
    for segment in config['segments']:
        this_segment_start = segment[0] * 1000
        this_segment_end = segment[1] * 1000
        this_segment_duration = this_segment_end - this_segment_start
        if this_segment_duration > 0:
            segments.append([this_segment_start, this_segment_end, this_segment_duration, 'voiced'])
        else:
            print(f"segment start {this_segment_start} is greater than segment end {this_segment_end}")

    i = 0
    for segment in segments:
        if segment[3] == 'voiced':
            print(f"{Fore.GREEN}.. {i:>3}. {segment[3]} - {(segment[0]/1000):6.2f} : {(segment[1]/1000):6.2f}  -  duration : {(segment[2]/1000):6.2f}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}.. {i:>3}. {segment[3]} - {(segment[0]/1000):6.2f} : {(segment[1]/1000):6.2f}  -  duration : {(segment[2]/1000):6.2f}{Style.RESET_ALL}")

        i = i + 1

    print()


    # split by segments
    audio_files = split_segments(sound, segments, config)


    # do the asr
    do_asr_on_files(audio_files)

    return audio_files



''' do the processing
'''
def process_automatically(config):

    # open as sound
    sound = open_as_sound(config)
    print(printable_info(sound, config['input-audio-file']))


    # filter sound
    sound = filter(sound, config)
    print(printable_info(sound, config['input-audio-file']))


    # identify silent segments
    segments, silent_segment_count, voiced_segment_count  = identify_segments(sound, config)
    print(f".. {silent_segment_count} silent segments found")
    print(f".. {voiced_segment_count} voiced segments found")

    i = 0
    for segment in segments:
        if segment[3] == 'voiced':
            print(f"{Fore.GREEN}.. {i:>3}. {segment[3]} - {(segment[0]/1000):6.2f} : {(segment[1]/1000):6.2f}  -  duration : {(segment[2]/1000):6.2f}{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}.. {i:>3}. {segment[3]} - {(segment[0]/1000):6.2f} : {(segment[1]/1000):6.2f}  -  duration : {(segment[2]/1000):6.2f}{Style.RESET_ALL}")

        i = i + 1

    print()


    # split by segments
    audio_files = split_segments(sound, segments, config)


    # do the asr
    if config['do-asr']:
        do_asr_on_files(audio_files)

    return audio_files



''' write output
'''
def write_output(config, audio_files):
    # write output
    with open(config['asr-output-file'], "w", encoding="utf-8") as f:
        for audio_file in audio_files:
            if 'asr-response' in audio_file:
                f.write(f"audio        : {audio_file['file']}")
                f.write('\n')

                f.write(f"duration     : {audio_file['duration']:6.2f} secoonds, {audio_file['asr-response']['processingTime']}")
                f.write('\n')

                f.write(audio_file['asr-response']['text'])
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
        audio_files = process_manually(config)
    else:
        audio_files = process_automatically(config)

    write_output(config, audio_files)