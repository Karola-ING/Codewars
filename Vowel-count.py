# https://www.codewars.com/kata/54ff3102c1bad923760001f3

def get_count(sentence):
    vowels = ['a','e', 'i', 'o', 'u']

    vowels_count = 0
    for letter in sentence:
        if letter in vowels:
            vowels_count += 1
    
    return vowels_count

sentence = 'abracadabra'
print(get_count(sentence))