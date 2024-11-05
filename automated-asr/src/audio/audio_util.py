#!/usr/bin/env python3

import json
import requests
from pydub import AudioSegment, silence, scipy_effects

from audio.segment import Segment, MergeSegments
from helper.logger import *


''' return sound object from the input audio file
'''
def open_as_sound(config):
    segments = []

    input_audio_file = config.input_audio_file
    sound = AudioSegment.from_wav(input_audio_file)
    info('source audio info')
    info('-------------------------------------------------')
    print(printable_info(sound, input_audio_file))

    channels = sound.split_to_mono()
    sound = channels[0]

    return sound



''' apply filters as specified in the config
'''
def filter(config, sound):
    if config.high_pass_filter_enabled:
        sound = scipy_effects.high_pass_filter(sound, cutoff_freq=config.high_pass_filter_frequency, order=config.high_pass_filter_order)
        info(f"filtered sound file info - CUT BELOW {config.high_pass_filter_frequency} Hz")
        info('----------------------------------------------------------------------------------')
        print(printable_info(sound, config.input_audio_file))


    if config.low_pass_filter_enabled:
        sound = scipy_effects.low_pass_filter(sound, cutoff_freq=config.low_pass_filter_frequency, order=config.low_pass_filter_order)
        info(f"filtered sound file info - CUT ABOVE {config.low_pass_filter_frequency} Hz")
        info('--------------------------')
        print(printable_info(sound, config.input_audio_file))

    return sound



''' merge segments
'''
def merge_segments(config, segments):
    # then we handle smaller segments to merge them into optimal size segments
    merged_segments = []
    merge_segment = None
    for current_segment in segments:
        # it may be that this current segment is a large one
        if current_segment.duration_ms > config.optimal_audio_ms:

            # we have an active MergeSegments
            if merge_segment:
                # close the MergeSegments
                merged_segments.append(merge_segment.merge())
                merge_segment = None

            # we do not have an active MergeSegments
            else:
                pass

            merged_segments.append(current_segment)

        # this is not a large segment, try to include this segment into the merge
        else:
            # we already have a MergeSegments active, try to append to it
            if merge_segment:
                # this segment fits within the merge
                if merge_segment.append(current_segment) == True:
                    pass

                # this segment does not fit within the merge
                else:
                    # close the MergeSegments
                    newly_merged_segment = merge_segment.merge()
                    if newly_merged_segment:
                        merged_segments.append(newly_merged_segment)

                    # create a new MergeSegments and append to it
                    merge_segment = MergeSegments(config.optimal_audio_ms)
                    merge_segment.append(current_segment)

            # we do not have a MergeSegments active, create one and append to it
            else:
                merge_segment = MergeSegments(config.optimal_audio_ms)
                merge_segment.append(current_segment)

    # there may be an open MergeSegments, close it
    if merge_segment:
        newly_merged_segment = merge_segment.merge()
        if newly_merged_segment:
            merged_segments.append(newly_merged_segment)


    return sorted(merged_segments)



''' split into separate files as specified by the segments
'''
def split_segments(segments):
    index = 0
    for segment in segments:
        segment.export(index=index)
        index = index + 1



''' generate printable info for the audio file
'''
def printable_info(sound, audio_file_name, left_padding='    '):
    str = f"\n{left_padding}audio file    : {audio_file_name}"
    str = f"{str}\n{left_padding}duration (s)  : {sound.duration_seconds:3.2f}"
    str = f"{str}\n{left_padding}channels      : {sound.channels}"
    str = f"{str}\n{left_padding}loudness      : {sound.dBFS} dBFS"
    str = f"{str}\n{left_padding}sample width  : {sound.sample_width} byte(s)"
    str = f"{str}\n{left_padding}frame rate    : {sound.frame_rate}"
    str = f"{str}\n{left_padding}max amplitude : {sound.max}"
    str = f"{str}\n{left_padding}max loudness  : {sound.max_dBFS}"
    str = f"{str}\n\n"

    return str



''' bulk asr on a list of files
'''
def do_asr_on_files(segments):
    for segment in segments:
        if segment.content == 'voiced':
            info(f".. doing asr on {segment.file}")
            segment.asr_response = get_text_from_audio(segment.file)



''' asr from audio
'''
def get_text_from_audio(audio_file_path, reference_text=None):
    files = {'file': open(audio_file_path, 'rb')}
    payload = {'format': 'wav'}
    response = requests.post(
        "https://nlp.celloscope.net/nlp/speech-to-text/v2",
        files=files,
        data=payload
    )
    print(response.text)

    json_response = json.loads(response.text)
    return json_response
