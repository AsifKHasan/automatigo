#!/usr/bin/env python3

import os
import yaml
from pathlib import Path

from helper.logger import *

''' Configuration object
'''
class Config(object):

    ''' constructor
    '''
    def __init__(self, config_path):
        config_path = Path(config_path).resolve()
        config = yaml.load(open(config_path, 'r', encoding='utf-8'), Loader=yaml.FullLoader)
        self.log_level = config['log-level']
        self.output_dir = config['output-dir']
        self.asr_output_file = config['asr-output-file']
        self.audio_data_dir = f"{self.output_dir}/audio"
        self.audio_out_dir = f"{self.audio_data_dir}/splits"

        self.optimal_audio_ms = config['optimal-audio-seconds'] * 1000

        self.max_silence_len = config['max-silence-len']
        self.min_silence_len = config['min-silence-len']
        self.silence_len_decrement_by = config['silence-len-decrement-by']

        self.min_silence_thresh = config['min-silence-thresh']
        self.max_silence_thresh = config['max-silence-thresh']
        self.silence_thresh_increment_by = config['silence-thresh-increment-by']

        self.adjust_len_before_thresh = config['adjust-len-before-thresh']

        self.seek_step = config['seek-step']

        self.audio_ms_to_keep_before = config['audio-ms-to-keep-before']
        self.audio_ms_to_keep_after = config['audio-ms-to-keep-after']

        self.high_pass_filter_enabled = config['high-pass-filter']['enabled']
        self.high_pass_filter_frequency = config['high-pass-filter']['frequency']
        self.high_pass_filter_order = config['high-pass-filter']['order']

        self.low_pass_filter_enabled = config['low-pass-filter']['enabled']
        self.low_pass_filter_frequency = config['low-pass-filter']['frequency']
        self.low_pass_filter_order = config['low-pass-filter']['order']

        self.audio_range = [0, 0]
        self.do_asr = config['do-asr']


    ''' configure environment
    '''
    def configure(self, file_name, range_spec, segment_spec):

        # determine base name and extension of audio file
        self.input_audio_file = f"{self.audio_data_dir}/{file_name}"

        self.input_audio_file_base_name, self.input_audio_file_type = os.path.splitext(file_name)
        debug(f"[{file_name}] is of type [{self.input_audio_file_type}]")

        self.output_file_format = f"{self.audio_out_dir}/{self.input_audio_file_base_name}-" + '{}-{}__{}-{}.wav'

        self.asr_output_file = f"{self.output_dir}/{self.asr_output_file}"

        # range
        debug(f"checking range [{range_spec}]")
        if range_spec:
            splitted = range_spec.split(':')
            if len(splitted) == 2:
                # start range
                if splitted[0] == '':
                    debug(f"empty start range found, assuming start-of-audio")
                    range_start = 0.0
                else:
                    try:
                        range_start = float(splitted[0])
                    except:
                        print(f"can not convert start range {splitted[0]} to a number, assuming start-of-audio")
                        range_start = 0.0

                self.audio_range[0] = range_start

                # end range
                if splitted[1] == '':
                    debug(f"empty end range found, assuming end-of-audio")
                    range_end = 0.0
                else:
                    try:
                        range_end = float(splitted[1])
                        self.audio_range[1] = range_end
                    except:
                        print(f"can not convert end range {splitted[1]} to a number, assuming end-of-audio")
                        range_end = 0.0

            else:
                warn(f"range [{range_spec}] is not valid .. processing full audio")

        else:
            info(f"range [{range_spec}] is not provided .. processing full audio")

        # segments
        segment_list = []
        if segment_spec:
            if segment_spec == "NOSEG":
                # there will be only one segment with the full range specified
                self.segments = [[0, self.audio_range[1] - self.audio_range[0]]]

            else:
                pairs = segment_spec.split(' ')
                if len(pairs) > 1:
                    for pair in pairs:
                        splitted = pair.split(':')
                        if len(splitted) == 2:
                            try:
                                segment_start = float(splitted[0])
                            except:
                                print(f"can not convert {splitted[0]} to a number")
                                continue

                            try:
                                segment_end = float(splitted[1])
                            except:
                                print(f"can not convert {splitted[1]} to a number")
                                continue

                            segment_list.append([segment_start, segment_end])

                        else:
                            print(f"can not determine range from : {pair}")
                            continue

                self.segments = sorted(segment_list)
                print(self.segments)

        else:
            self.segments = None



    ''' get the next segmentation parameter (silence_len, silence_thresh)
    '''
    def get_next_silence_parameter(self, silence_len, silence_thresh, length_first=True):
        if length_first:
            possible_silence_len = silence_len - self.silence_len_decrement_by
            if possible_silence_len >= self.min_silence_len:
                return possible_silence_len, silence_thresh

            else:
                possible_silence_thresh = silence_thresh + self.silence_thresh_increment_by
                if possible_silence_thresh <= self.max_silence_thresh:
                    return silence_len, possible_silence_thresh

                else:
                    return None, None
        else:
            possible_silence_thresh = silence_thresh + self.silence_thresh_increment_by
            if possible_silence_thresh <= self.max_silence_thresh:
                return silence_len, possible_silence_thresh

            else:
                possible_silence_len = silence_len - self.silence_len_decrement_by
                if possible_silence_len >= self.min_silence_len:
                    return possible_silence_len, silence_thresh

                else:
                    return None, None
