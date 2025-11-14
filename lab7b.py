#!/usr/bin/env python3
"""
OPS445 Lab 7 - Lab7b
Time class with special methods and time manipulation
"""

class Time:
    """Simple object type for time of the day.
       Data attributes: hours, minutes, seconds
    """
    def __init__(self, hours=12, minutes=0, seconds=0):
        """Constructor for Time object"""
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def __str__(self):
        """Return time as a formatted string"""
        return f"{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}"

    def __add__(self, other):
        """Add two Time objects"""
        if not isinstance(other, Time):
            return NotImplemented

        new_time = Time()
        new_time.hours = self.hours + other.hours
        new_time.minutes = self.minutes + other.minutes
        new_time.seconds = self.seconds + other.seconds

        # Normalize seconds → minutes
        while new_time.seconds >= 60:
            new_time.seconds -= 60
            new_time.minutes += 1

        # Normalize minutes → hours
        while new_time.minutes >= 60:
            new_time.minutes -= 60
            new_time.hours += 1

        # Wrap hours to 0–23
        new_time.hours %= 24

        return new_time

    def is_valid(self):
        """Return True if the time attributes are within valid ranges"""
        return (
            0 <= self.hours < 24 and
            0 <= self.minutes < 60 and
            0 <= self.seconds < 60
        )

# ----------------------------
# Extra functions for lab
# ----------------------------

def format_time(time_obj):
    """Return a Time object as a formatted string"""
    if not isinstance(time_obj, Time):
        raise TypeError("Argument must be a Time object")
    return f"{time_obj.hours:02d}:{time_obj.minutes:02d}:{time_obj.seconds:02d}"

def change_time(time_obj, seconds):
    """Modify a Time object by adding/subtracting seconds"""
    if not isinstance(time_obj, Time):
        raise TypeError("First argument must be a Time object")

    # Convert total time to seconds
    total_seconds = time_obj.hours * 3600 + time_obj.minutes * 60 + time_obj.seconds
    total_seconds += seconds

    # Normalize within a day (0–86399 seconds)
    total_seconds %= 86400

    # Convert back to hours, minutes, seconds
    time_obj.hours = total_seconds // 3600
    time_obj.minutes = (total_seconds % 3600) // 60
    time_obj.seconds = total_seconds % 60

    return None
