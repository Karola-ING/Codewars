def min_sum(arr):

    list = sorted(arr)

    sum = 0
    for index in range(len(list)):
        sum += list[-index-1] * list[index]
    return sum/2
     