# https://www.codewars.com/kata/52efefcbcdf57161d4000091

def count(string):
    no_duplicates_list = []

    for element in string:
        if element not in no_duplicates_list:
            no_duplicates_list.append(element)

    dictionary = dict.fromkeys(no_duplicates_list, 0)

    for element in list(string):
        for key, value in dictionary.items():
            if element == key:
                dictionary[key] = value + 1
    
    return dictionary

string = 'abahshshsa'
print(count(string))