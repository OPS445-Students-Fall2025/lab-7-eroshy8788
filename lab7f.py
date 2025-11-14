#!/usr/bin/env python3
# Student ID: eroshy

class Time:
    """Simple object type for time of the day.
       Data attributes: hour, minute, second
       Function attributes: __init__, __str__, __repr__,
                            time_to_sec, format_time,
                            change_time, sum_times, __add__
    """

    def __init__(self, hour=12, minute=0, second=0):
        """Constructor for Time object"""
        self.hour = hour
        self.minute = minute
        self.second = second

    # ---------------- Methods ----------------

    def format_time(self):
        """Return time object as a formatted string"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def sum_times(self, t2):
        """Add two Time objects and return the sum"""
        sum_obj = Time()
        sum_obj.hour = self.hour + t2.hour
        sum_obj.minute = self.minute + t2.minute
        sum_obj.second = self.second + t2.second

        # Carry over seconds → minutes
        while sum_obj.second >= 60:
            sum_obj.second -= 60
            sum_obj.minute += 1

        # Carry over minutes → hours
        while sum_obj.minute >= 60:
            sum_obj.minute -= 60
            sum_obj.hour += 1

        return sum_obj

    def change_time(self, seconds):
        """Modify the current Time object by adding seconds"""
        total_seconds = self.time_to_sec() + seconds
        new_time = sec_to_time(total_seconds)
        self.hour, self.minute, self.second = new_time.hour, new_time.minute, new_time.second
        return None

    def time_to_sec(self):
        """Convert the Time object to total seconds from midnight"""
        return self.hour * 3600 + self.minute * 60 + self.second

    def valid_time(self):
        """Check if the Time object is valid"""
        if self.hour < 0 or self.minute < 0 or self.second < 0:
            return False
        if self.hour >= 24 or self.minute >= 60 or self.second >= 60:
            return False
        return True

    # -------- Special Methods --------

    def __str__(self):
        """String representation used by print()"""
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

    def __repr__(self):
        """String representation used in interactive shell"""
        return f'{self.hour:02d}.{self.minute:02d}.{self.second:02d}'

    def __add__(self, t2):
        """Overload the '+' operator to add two Time objects"""
        return self.sum_times(t2)


# ------------- External Function -------------
def sec_to_time(seconds):
    """Convert total seconds to a Time object"""
    t = Time()
    minutes, t.second = divmod(seconds, 60)
    t.hour, t.minute = divmod(minutes, 60)
    return t
