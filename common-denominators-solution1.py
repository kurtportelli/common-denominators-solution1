def convertFracts(lst):
    if not lst:
        return lst
    
    from functools import reduce
    dens = []
    for num, den in lst:
        dens.append(den)
    lcd = reduce(lcm, dens)
    lst = [[lcd * num // den, lcd] for num, den in lst]
    return lst
    
def gcd(a, b):
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)
