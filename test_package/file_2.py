
def function_b(value):
    if value < 0:
        return value - 1
    else:
        value2 = subfunction_b(value + 1)
        return value + value2
    
def subfunction_b(inp):
    vals_to_accum = []
    for i in range(10):
        vals_to_accum.append(inp ** (i/10))
    if vals_to_accum[-1] > 2:
        vals.append(100)
    # really you would use numpy to do this kind of number-crunching... but we're doing this for the sake of example right now
    return sum(vals_to_accum) 
