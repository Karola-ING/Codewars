def filter_long_words(sentence, n):
    sentence_list = sentence.split(" ") 

    n_list = []
    for element in sentence_list:
        if len(element) <= n:
            continue
        else:
            n_list.append(element)
    return n_list


print(filter_long_words("The quick brown fox jumps over the lazy dog", 4))