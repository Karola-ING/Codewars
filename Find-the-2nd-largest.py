def find_2nd_largest(arr):

    string_arr = []
    for element in arr:
        if type(element) == int or type(element) == float:
            continue
        else:
            string_arr.append(element)

    for element in string_arr:
        arr.remove(element)

    result = arr.count(arr[0]) == len(arr)
    if result:
        return None
    else:
        arr_sorted = sorted(arr)
        sec_largest_elem = arr_sorted[-2]
        return sec_largest_elem

print(find_2nd_largest([1,1,1,1,1,1,1]))