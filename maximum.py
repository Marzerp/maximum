#!/usr/bin/env pyhton3

#Maximum algorythm
#By Marzerp
#LICENSE GNU/GPL

data= [1.0, 3.14, 6.2, 0.1, 5.3]

maximum= -99999.999

for x in data:
    if x>maximum:
        maximum = x
        
print(maximum)
