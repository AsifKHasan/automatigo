#!/usr/bin/env python3

import sys
import json
import yaml
import datetime
import argparse
from pathlib import Path

from audio.audio_util import *

CONFIG_PATH = '../conf/config.yml'


''' do the processing
'''
def process(config):

    # opne as sound
    sound = open_as_sound(config)
    print(printable_info(sound, config['input-audio-file']))

    # identify segments

    # split by segments

    # do the asr

    # write output
    # with open('out.txt', "w", encoding="utf-8") as f:
    #     for audio_file in audio_files:
    #         f.write(f"audio    : {audio_file['file']}")
    #         f.write('\n')

    #         f.write(f"duration : {audio_file['duration']:6.2f} secoonds")
    #         f.write('\n')

    #         json_response = get_text_from_audio(audio_file['file'])
    #         audio_file['text'] = json_response['text']
    #         audio_file['seconds'] = json_response['processingTime']

    #         f.write(audio_file['seconds'])
    #         f.write('\n')

    #         # f.write(audio_file['text'].encode('utf-8').decode(sys.stdout.encoding))
    #         f.write(audio_file['text'])
    #         f.write('\n\n')



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

    return config



if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-a", "--audio", required=True, help="audio file name to process, without extension, wav assumed")
    args = vars(ap.parse_args())
    config = configure(args["audio"])
    process(config)
