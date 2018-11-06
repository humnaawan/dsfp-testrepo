
# `math` here is for *scalar* math... normally you'd use numpy but this makes it a bit simpler to debug

import math 

inf = float('inf')  # this is a quick-and-easy way to get the "infinity" value 

def function_a(angle=180):
    if angle%180==0:
        return inf
    anglerad = math.radians(angle)
    return math.sin(anglerad/2)/math.sin(anglerad)
