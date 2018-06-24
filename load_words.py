import pickle

def is_valid_word(word):
    # no proper nouns
    return word[0].islower()

def load_words():
    words_file = '/usr/share/dict/words'
    valid_words = []
    with open(words_file) as words:
        for word in words:
            if is_valid_word(word):
                valid_words.append(word)

    with open('words.pkl', 'wb') as valid_words_file:
        pickle.dump(valid_words, valid_words_file)