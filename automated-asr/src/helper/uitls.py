#!/usr/bin/env python3

import math

'''
'''
def ms_to_text(ms):
    ms_int = int(ms)
    miliseconds = ms_int % 1000
    seconds = int((ms_int - miliseconds) % 60)
    return seconds, miliseconds
    
