#!/usr/bin/env python3
"""
OPS445 Lab 7 - Lab7c
Time class with functions using seconds for computation
"""

class Time:
    """Simple object type for time of the day"""
    def __init__(self, hours=12, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

# ----------------------------
# Helper functions
# ----------------------------

def format_time(time_obj):
    """Return a Time object as a formatted string"""
    if not isinstance(time_obj, Time):
        raise TypeError("Argument must be a Time object")
    return f"{time_obj.hours:02d}:{time_obj.minutes:02d}:{time_obj.seconds:02d}"

def time_to_sec(time_obj):
    """Convert a Time object to total seconds since midnight"""
    return time_obj.hours * 3600 + time_obj.minutes * 60 + time_obj.seconds

def sec_to_time(seconds):
    """Convert total seconds (0–86399) to a Time object"""
    seconds %= 86400  # wrap after 24h
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    sec = seconds % 60
    return Time(hours, minutes, sec)

def sum_times(t1, t2):
    """Add two Time objects and return a new Time object"""
    total_seconds = time_to_sec(t1) + time_to_sec(t2)
    return sec_to_time(total_seconds)

def change_time(time_obj, seconds):
    """Modify a Time object by adding/subtracting seconds"""
    total_seconds = time_to_sec(time_obj) + seconds
    new_time = sec_to_time(total_seconds)
    time_obj.hours = new_time.hours
    time_obj.minutes = new_time.minutes  # fixed typo
    time_obj.seconds = new_time.seconds
    return None

