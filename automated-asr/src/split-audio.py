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
def process(config):

    # opne as sound
    sound = open_as_sound(config)
    print(printable_info(sound, config['input-audio-file']))


    # identify silent segments
    silent_segments = identify_silent_segments(sound, config)
    print(f".. {len(silent_segments)} silent segments found")

    # identify non-silent segments
    nonsilent_segments = identify_nonsilent_segments(sound, config)
    print(f".. {len(nonsilent_segments)} voiced segments found")

    segments = sorted(nonsilent_segments + silent_segments)

    i = 0
    for segment in segments:
        if segment[3] == 'voiced':
            print(f"{Fore.GREEN}.. {i:>3}. {segment[3]} - {(segment[0]/1000):6.2f} : {(segment[1]/1000):6.2f}  -  duration : {(segment[2]/1000):6.2f}")
        else:
            print(f"{Fore.RED}.. {i:>3}. {segment[3]} - {(segment[0]/1000):6.2f} : {(segment[1]/1000):6.2f}  -  duration : {(segment[2]/1000):6.2f}")

        i = i + 1

    print()


    # split by segments
    audio_files = split_segments(sound, segments, config)


    # do the asr
    do_asr_on_files(audio_files)


    # write output
    with open(config['asr-output-file'], "w", encoding="utf-8") as f:
        for audio_file in audio_files:
            if 'asr-response' in audio_file:
                f.write(f"audio        : {audio_file['file']}")
                f.write('\n')

                f.write(f"duration     : {audio_file['duration']:6.2f} secoonds")
                f.write('\n')

                f.write(f"processed in : {audio_file['asr-response']['processingTime']}")
                f.write('\n')

                # f.write(audio_file['text'].encode('utf-8').decode(sys.stdout.encoding))
                f.write(audio_file['asr-response']['text'])
                f.write('\n\n')



''' configure environment
'''
def configure(file_name):
    config_path = Path(CONFIG_PATH).resolve()
    config = yaml.load(open(config_path, 'r', encoding='utf-8'), Loader=yaml.FullLoader)
    output_dir = config['output-dir']
    config['audio-data-dir'] = f"{output_dir}/audio"
    config['audio-out-dir'] = f"{config['audio-data-dir']}/splits"

    config['input-audio-file'] = f"{config['audio-data-dir']}/{file_name}.wav"
    config['output-file-format'] = f"{config['audio-out-dir']}/{file_name}-"

    config['asr-output-file'] = f"{config['output-dir']}/{config['asr-output-file']}"

    return config



if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-a", "--audio", required=True, help="audio file name to process, without extension, wav assumed")
    args = vars(ap.parse_args())
    config = configure(args["audio"])
    process(config)