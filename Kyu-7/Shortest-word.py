# https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9

def number_list(s):
    word_list = list(s.split(" "))

    number_list = []
    for element in word_list:
        number = 0
        for letter in element:
            number += 1 
        number_list.append(number)
        
    return number_list


def find_short(s):
    final_list = number_list(s)
    l = min(final_list)
        
    return l

print(find_short('bitcoin take'))
print(find_short('bitcoin take over the world maybe who knows perhaps'))
