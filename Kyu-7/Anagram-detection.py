# https://www.codewars.com/kata/529eef7a9194e0cbc1000255

def is_anagram(test, original):
    
    original_list = []
    for letter in original.lower():
        original_list.append(letter)
        
    test_list = []
    for letter in test.lower():
        test_list.append(letter)
    
    result = sorted(test_list) == sorted(original_list)
    
    if result:
        return True
    else:
        return False