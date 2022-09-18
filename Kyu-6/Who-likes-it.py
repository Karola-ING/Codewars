# https://www.codewars.com/kata/5266876b8f4bf2da9b000362

def likes(names):
    if names == []:
        return f'no one likes this'
    if len(names) == 1:
        return f'{names[0]} likes this'
    if len(names) == 2:
        return f'{names[0]} and {names[1]} like this'
    if len(names) == 3:
        return f'{names[0]}, {names[1]} and {names[2]} like this'
    if len(names) >= 4:
        number = len(names) - 2
        return f'{names[0]}, {names[1]} and {number} others like this'


names = ['Peter']
names2 = ['Jacob', 'Alex']
names3 = ['Max', 'John', 'Mark']
names4 = ['Alex', 'Jacob', 'Mark', 'Max']
print(likes(names))
print(likes(names2))
print(likes(names3))
print(likes(names4))