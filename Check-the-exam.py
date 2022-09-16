# https://www.codewars.com/kata/5a3dd29055519e23ec000074

def check_exam(arr1,arr2):
    result = 0
    for element in range(4):
        if arr1[element] == arr2[element]:
            result += 4
        elif arr2[element] == '':
            result += 0
        else:
            result -=1

        
    if result < 0:
        result = 0
    return result

print(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]))