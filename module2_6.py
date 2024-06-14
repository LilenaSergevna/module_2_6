def single_root_words (root_word, *other_words):
    same_words=[]
    for i in other_words:
        x = root_word.upper()
        y = i.upper()
        if len(root_word)<len(i):
            pos=y.find(x)
        else:
            pos = x.find(y)
        if pos!=-1:
            same_words.append(i)
    return same_words



result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)