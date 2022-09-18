# https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097

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