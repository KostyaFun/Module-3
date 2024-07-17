def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if root_word.upper() in word.upper() or word.upper() in root_word.upper():
            same_words.append(word)
    print(same_words)
single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
