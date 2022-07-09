#!/usr/bin/env python3

from pydub import AudioSegment, silence, scipy_effects

from helper.logger import *


''' Audio segment object
'''
class Segment(object):

    ''' constructor
    '''
    @classmethod
    def from_sound(cls, sound, config):
        return cls(sound=sound, config=config, start_ms=0, end_ms=len(sound), content='voiced', at_silence_len=config.max_silence_len, at_silence_thresh=config.min_silence_thresh)



    ''' constructor
    '''
    def __init__(self, sound, config, start_ms, end_ms, content, at_silence_len=None, at_silence_thresh=None):
        self.sound, self.config, self.start_ms, self.end_ms, self.content, self.at_silence_len, self.at_silence_thresh = sound, config, start_ms, end_ms, content, at_silence_len, at_silence_thresh
        self.duration_ms = self.end_ms - self.start_ms
        self.segment_sound = self.sound[self.start_ms:self.end_ms]
        self.asr_response = None
        self.file = None
        self.broken_down_segments = []



    ''' get broken down segment
    '''
    def get_broken_down_segments(self):
        if len(self.broken_down_segments) == 0:
            return [self]

        else:
            segments = []
            for segment in self.broken_down_segments:
                segments.extend(segment.get_broken_down_segments())

            return segments


    ''' break down segment
    '''
    def break_down(self):
        # if the segment is already under the optimmum length, it need not be broken down
        if self.duration_ms <= self.config.optimal_audio_ms:
            return

        while True:
            print()
            info(f"breaking {self} with min_silence {self.at_silence_len} ms and silence_thresh {self.at_silence_thresh} dB")
            segments = self.break_by_silence()
            if segments:
                debug(f".. broke down segment  {self} into {len(segments)} segments")
                self.broken_down_segments = segments
                break
            else:
                warn(f".. couldn't break down {self} further")

                # try with next silence_parameter
                next_silence_len, next_silence_thresh = self.config.get_next_silence_parameter(self.at_silence_len, self.at_silence_thresh, length_first=self.config.adjust_len_before_thresh)
                if next_silence_len is not None and next_silence_thresh is not None:
                    self.at_silence_len, self.at_silence_thresh = next_silence_len, next_silence_thresh
                else:
                    # we can not decrease the silence length any more
                    warn(f".. {self} - all silence parameters exhausted")
                    return

        # we may have a list of broken_down_segments, we need to break them down 
        for segment in self.broken_down_segments:
            segment.break_down()



    ''' break down a segment into silent and voiced segments
    '''
    def break_by_silence(self):
        # silent segments
        silents = silence.detect_silence(self.segment_sound, min_silence_len=self.at_silence_len, silence_thresh=self.at_silence_thresh, seek_step=self.config.seek_step)
        
        # if there is no silent segments, it means we can not break it down
        if len(silents) == 0:
            return None

        segments = [Segment(sound=self.sound, config=self.config, start_ms=(self.start_ms + s[0]), end_ms=(self.start_ms + s[1]), content='silent', at_silence_len=self.at_silence_len, at_silence_thresh=self.at_silence_thresh) for s in silents]

        # non-silent segments
        voiceds = silence.detect_nonsilent(self.segment_sound, min_silence_len=self.at_silence_len, silence_thresh=self.at_silence_thresh, seek_step=self.config.seek_step)
        for s in voiceds:
            segment_start, segment_end = self.start_ms + s[0], self.start_ms + s[1]

            segment_start = segment_start - self.config.audio_ms_to_keep_before
            if segment_start < self.start_ms:
                segment_start = self.start_ms
                
            segment_end = segment_end + self.config.audio_ms_to_keep_after
            if segment_end > self.end_ms:
                segment_end = self.end_ms

            segments.append(Segment(sound=self.sound, config=self.config, start_ms=segment_start, end_ms=segment_end, content='voiced', at_silence_len=self.at_silence_len, at_silence_thresh=self.at_silence_thresh))

        segments = sorted(segments)
        # print(f".. break_by_silence : {', '.join(s.to_string() for s in segments)}")

        return segments



    ''' string representation
    '''
    def __repr__(self):
        s = f"{self.content} - [{(self.start_ms/1000):6.2f} : {(self.end_ms/1000):6.2f}]  -  duration : {(self.duration_ms/1000):6.2f} at {self.at_silence_len} ms, {self.at_silence_thresh} dB"
        return s



    ''' short string representation
    '''
    def to_string(self):
        return f"[{(self.start_ms/1000):6.2f} : {(self.end_ms/1000):6.2f}]"



    ''' operator <
    '''
    def __lt__(self, other):
        return self.start_ms < other.start_ms



    ''' export to wav
    '''
    def export(self, index):
        output_file = self.config.output_file_format.format(index, self.content)
        chunk = self.sound[self.start_ms:self.end_ms]
        # chunk = chunk.apply_gain(+1.0)
        chunk.export(output_file, format="wav")
        self.file = output_file



''' Mergeable Segments
'''
class MergeSegments(object):

    ''' constructor
    '''
    def __init__(self, optimal_audio_ms):
        self.optimal_audio_ms = optimal_audio_ms
        self.segments = []



    ''' string representation
    '''
    def __repr__(self):
        lines = [f"duration {self.duration_ms()/1000:6.2f}s"]
        for segment in self.segments:
            lines.append(f"[{(segment.start_ms/1000):6.2f} : {(segment.end_ms/1000):6.2f}]")

        return ', '.join(lines)



    ''' merge method
        if duration is within range append and return True
    '''
    def merge(self):
        if len(self.segments):
            return Segment(sound=self.segments[0].sound, config=self.segments[0].config, start_ms=self.start_ms(), end_ms=self.end_ms(), content='voiced', at_silence_len=self.segments[0].at_silence_len, at_silence_thresh=self.segments[0].at_silence_thresh)
        else:
            warn(f".... can not merge an empty MergeSegments")
            return None
        


    ''' append method
        if duration is within range append and return True
    '''
    def append(self, segment):
        if len(self.segments):
            if (segment.end_ms - self.start_ms()) <= self.optimal_audio_ms:
                # warn(f".... appending {segment} into {self}")
                self.segments.append(segment)
                return True
            else:
                # warn(f".... can not append {segment} into {self}")
                return False

        else:
            if segment.duration_ms <= self.optimal_audio_ms:
                # warn(f".... appending {segment} into {self}")
                self.segments.append(segment)
                return True
            else:
                # warn(f".... can not append {segment} into {self}")
                return False



    ''' merge start in ms
    '''
    def start_ms(self):
        if len(self.segments):
            return self.segments[0].start_ms
        else:
            return -1



    ''' merge end in ms
    '''
    def end_ms(self):
        if len(self.segments):
            return self.segments[-1].end_ms
        else:
            return -1



    ''' merge end in ms
    '''
    def duration_ms(self):
        if len(self.segments):
            return self.segments[-1].end_ms - self.segments[0].start_ms
        else:
            return -1


   