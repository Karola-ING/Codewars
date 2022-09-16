import math

def century(year):
    century = 0
    if year <= 100:
        century = 1
    if year >= 101:
        x = year / 100
        x = math.ceil(x)
        century = x 
    return century 