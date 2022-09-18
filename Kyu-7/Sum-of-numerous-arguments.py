# https://www.codewars.com/kata/55c5b03f8c28da9a51000045

def find_sum(*args):
    sum = 0
    for number in args:
        if number < 0:
            return -1
        else:
            sum += number
    return sum