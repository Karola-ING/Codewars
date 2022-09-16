def my_retrurn(number):
    special_nums = [0, 1, 2, 3, 4, 5]
    test_nums = []
    for digit in str(number):
        test_nums.append(int(digit))

    for digit in test_nums:
        if digit not in special_nums:
            return False
        else: 
            continue


def special_number(number):
    value = my_retrurn(number)
    if value == False:
        return "NOT!!"
    elif value == None:
        return "Special!!"
