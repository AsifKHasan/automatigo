#!/usr/bin/env python3

import math

''' milisecond to hours, minutes, seconds and miliseconds
'''
def ms_to_hmss(ms):
    ms_int = int(ms)
    seconds =(ms_int/1000) % 60
    seconds = int(seconds)
    minutes =(ms_int/(1000 * 60)) % 60
    minutes = int(minutes)
    hours = (ms_int/(1000 * 60 * 60)) % 24
    hours = int(hours)
    ms_int = ms_int % 1000

    return hours, minutes, seconds, ms_int
