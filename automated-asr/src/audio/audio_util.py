#!/usr/bin/env python3

import json
import requests
from pydub import AudioSegment, silence, scipy_effects

from audio.segment import Segment
from helper.logger import *



''' return sound object from the input audio file
'''
def open_as_sound(config):
    segments = []

    input_audio_file = config['input-audio-file']
    sound = AudioSegment.from_wav(input_audio_file)

    return sound



''' apply filters as specified in the config
'''
def filter(sound, config):

    new_sound = scipy_effects.high_pass_filter(sound, cutoff_freq=config['high-pass-filter']['frequency'], order=config['high-pass-filter']['order'])
    new_sound = scipy_effects.low_pass_filter(new_sound, cutoff_freq=config['low-pass-filter']['frequency'], order=config['low-pass-filter']['order'])

    return new_sound


''' optimize segments
'''
def optimize_segments(sound, segments_to_optimize, config):
    segments = sorted(segments_to_optimize)
    duration_in_ms = len(sound)

    silent_segment_count = 0
    voiced_segment_count = 0

    input_audio_file = config['input-audio-file']

    OPTIMAL_AUDIO_MS = config['OPTIMAL-AUDIO-SECONDS'] * 1000

    min_silence_len = config['min-silence-len']
    silence_thresh = config['silence-thresh']
    seek_step = config['seek-step']

    audio_ms_to_keep_before = config['audio-ms-to-keep-before']
    audio_ms_to_keep_after = config['audio-ms-to-keep-after']

    optimized_segments = []
    # first we handle larger segments to break them into optimal size segments
    current_segment_index = 0
    for current_segment in segments:
        if current_segment.content == 'voiced' and  current_segment.duration_ms > OPTIMAL_AUDIO_MS:
            warn(f"{current_segment.content} segment {current_segment_index:3} {current_segment.start_ms/1000:6.2f}:{current_segment.end_ms/1000:3.2f} duration is {current_segment.duration_ms/1000:3.2f}s .. optmizing ..")
        else:
            optimized_segments.append(current_segment)

        current_segment_index = current_segment_index + 1


    # then we handle smaller segments to merge them into optimal size segments

    return sorted(optimized_segments)


''' identify segments
'''
def identify_segments(sound, config):
    segments = []
    duration_in_ms = len(sound)

    input_audio_file = config['input-audio-file']

    OPTIMAL_AUDIO_SECONDS = config['OPTIMAL-AUDIO-SECONDS']

    min_silence_len = config['min-silence-len']
    silence_thresh = config['silence-thresh']
    seek_step = config['seek-step']

    audio_ms_to_keep_before = config['audio-ms-to-keep-before']
    audio_ms_to_keep_after = config['audio-ms-to-keep-after']


    # silent segments
    silents = silence.detect_silence(sound, min_silence_len=min_silence_len, silence_thresh=silence_thresh, seek_step=seek_step)
    segments = [Segment(start_ms=s[0], end_ms=s[1], content='silent') for s in silents]

    # non-silent segments
    voiceds = silence.detect_nonsilent(sound, min_silence_len=min_silence_len, silence_thresh=silence_thresh, seek_step=seek_step)
    for s in voiceds:
        segment_start, segment_end = s[0], s[1]

        segment_start = segment_start - audio_ms_to_keep_before
        if segment_start < 0:
            segment_start = 0
            
        segment_end = segment_end + audio_ms_to_keep_after
        if segment_end > duration_in_ms:
            segment_end = duration_in_ms

        segments.append(Segment(start_ms=segment_start, end_ms=segment_end, content='voiced'))

    
    # we may have segments which are not optimal
    segments = optimize_segments(sound, segments, config)

    return segments



''' split into separate files as specified by the segments
'''
def split_segments(sound, segments, config):
    output_file_format = config['output-file-format'] + '{:03}-{}.wav'
    index = 0
    for segment in segments:
        segment.export(sound=sound, output_file_format=output_file_format, index=index)
        index = index + 1

    return segments



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
    request_json = {
        'files': open(audio_file_path, 'rb')
    }

    response = requests.post(
        "https://nlp.celloscope.net/nlp/dataset/v1/audio/speech-to-text",
        data={'referenceText' : reference_text},
        files=request_json
    )

    json_response = json.loads(response.text)
    return json_response
