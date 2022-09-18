# https://www.codewars.com/kata/593b1909e68ff627c9000186

def nickname_generator(name):
    vovels = list('aeiou')
    name_list = list(name)
    length = len(name_list)
    print(length)

    if len(name_list) < 4:
        return 'Error: Name too short'
    else:
        if name_list[2] in vovels:
            nickname = ''.join(name_list[0:4])
            return nickname
        else:
            nickname = ''.join(name_list[0:3])
            return nickname
    
print(nickname_generator('Samm'))

