#!/usr/bin/env python3

import requests
from pydub import AudioSegment, silence


''' return sound object from the input audio file
'''
def open_as_sound(config):
    segments = []

    input_audio_file = config['input-audio-file']
    sound = AudioSegment.from_wav(input_audio_file)

    return sound



''' identify voice segments separated by silence
'''
def identify_voice_segments(config):
    segments = []

    input_audio_file = config['input-audio-file']

    MAX_AUDIO_SECONDS_ALLOWED = config['MAX-AUDIO-SECONDS-ALLOWED']
    MIN_AUDIO_SECONDS_ALLOWED = config['MIN-AUDIO-SECONDS-ALLOWED']
    
    return segments



''' split into separate files as specified by the segments
'''
def split_segments(sound, segments, config):
    output_files = []
    output_file_format = config['output-file-format'] + '{}.wav'
    i = 0
    for segment in segments:
        segment_start, segment_end = segment[0], segment[1]
        duration_seconds = (segment_end - segment_start) /1000
        output_file = output_file_format.format(i)
        chunk = sound[segment_start:segment_end]
        chunk.export(output_file, format="wav")
        output_files.append({'file': output_file, 'duration': duration_seconds, 'start': segment_start, 'end': segment_end})

    return output_files



''' generate printable info for the audio file
'''
def printable_info(sound, audio_file_name):
    str = ''
    str = f"{str}audio file    : {audio_file_name}\n"
    str = f"{str}duration (s)  : {sound.duration_seconds:6.2f}\n"
    str = f"{str}channels      : {sound.channels}\n"
    str = f"{str}loudness      : {sound.dBFS} dBFS\n"
    str = f"{str}sample width  : {sound.sample_width} byte(s)\n"
    str = f"{str}frame rate    : {sound.frame_rate}\n"
    str = f"{str}max amplitude : {sound.max}\n"
    str = f"{str}max loudness  : {sound.max_dBFS}\n"
    str = f"{str}\n\n"

    return str



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
