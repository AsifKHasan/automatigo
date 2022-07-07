#!/usr/bin/env python3

from pydub import AudioSegment, silence, scipy_effects

from helper.logger import *

''' Audio segment object
'''
class Segment(object):

    ''' constructor
    '''
    def __init__(self, start_ms, end_ms, content):
        self.start_ms, self.end_ms, self.content = start_ms, end_ms, content
        self.duration_ms = self.end_ms - self.start_ms
        self.asr_response = None



    ''' operator <
    '''
    def __lt__(self, other):
        return self.start_ms < other.start_ms



    ''' export to wav
    '''
    def export(self, sound, output_file_format, index):
        output_file = output_file_format.format(index, self.content)
        chunk = sound[self.start_ms:self.end_ms]
        chunk.export(output_file, format="wav")
        self.file = output_file
