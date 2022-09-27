# https://www.codewars.com/kata/554b4ac871d6813a03000035

def high_and_low(numbers):
    nums = numbers.split(' ')

    int_list = []
    for number in nums:
        int_list.append(int(number))

    max_value = max(int_list)
    min_value = min(int_list)
    print(sorted(int_list))
    return f'{max_value} {min_value}'

print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
