#!/usr/bin/env python3

#Maximum algorythm
#By: Marzerp
#LICENSE GNU/GPL

import sys

minimum= sys.float_info.max

data=[1.0, 3.14, 6.2, 0.1, 5.3]

for x in data:
    if x<minimum:
        minimum=x

print(minimum)
