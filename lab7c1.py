#!/usr/bin/env python3
# Student ID: [seneca_id]

from lab7c import *

# Original times
t1 = Time(8,0,0)
t2 = Time(8,55,0)
t3 = Time(9,50,0)

# Time delta
td = Time(0,50,0)

# Sum times
tsum1 = sum_times(t1, td)
tsum2 = sum_times(t2, td)

# Change t3 by seconds
change_time(t3, 1800)  # 1800 sec = 30 minutes

# Print results
ft = format_time
print(ft(t1), '+', ft(td), '-->', ft(tsum1))
print(ft(t2), '+', ft(td), '-->', ft(tsum2))
print('09:50:00 + 1800 sec -->', ft(t3))
