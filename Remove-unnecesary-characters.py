import string

def remove_char(array):
    disallowed_characters = string.printable
    disallowed_characters = disallowed_characters.replace('0123456789', '')

    new_array = []
    for element in array:
        for character in disallowed_characters:
            element = element.replace(character, '')
            continue
        print(element)
        new_array.append('$' + element[:-2] + '.' + element[-2:])
    
    return new_array
