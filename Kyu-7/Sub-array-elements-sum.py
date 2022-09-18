# https://www.codewars.com/kata/5b5e0ef007a26632c400002a

def numbers_list(arr, d=0):
    numbers = []
    for index in range(len(arr)):
        try:
            numbers.append(arr[index][len(arr) - 1 - index])
        except IndexError:
            numbers.append(d)
    return numbers
def final(numbers):
    sum = 0
    for number in numbers:
        sum += int(number)
    return sum
def elements_sum(arr, d=0):
    numbers_list(arr,d)
    return final(numbers_list(arr,d))