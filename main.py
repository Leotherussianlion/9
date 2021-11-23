def sort_sentence(sentence):
    sentence_local = sentence.lower()
    list_sentence_local = sentence_local.split(" ")
    for i in range(len(list_sentence_local)-1):
        k = i
        while len(list_sentence_local[k]) > len(list_sentence_local[k+1]):
            if k >= 0:
                list1 = list_sentence_local[k]
                list2 = list_sentence_local[k+1]           
                list_sentence_local[k: k+2] = [list2, list1]
                k -= 1
            else:
                break
    list_sentence_local = " ".join(list_sentence_local).capitalize()
    return list_sentence_local
