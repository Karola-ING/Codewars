def is_flush(cards):
    
    list = []
    for card in cards:
        list.append(card[-1])
    print(list)

    result = list.count(list[0]) == len(list)
    if result:
        return True
    else:
        return False
    

print(is_flush(["QD", "4D", "10D", "KD", "5D"]))