# https://www.codewars.com/kata/5a523566b3bfa84c2e00010b

def min_sum(arr):

    list = sorted(arr)

    sum = 0
    for index in range(len(list)):
        sum += list[-index-1] * list[index]
    return sum/2
     