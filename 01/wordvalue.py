from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, "r") as dictionary_file:
        whole_file = dictionary_file.read()
    word_list = whole_file.split('\n')
    word_list = word_list[:-1]
    return word_list


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    score = 0
    for letter in word:
        try:
            score += LETTER_SCORES[letter.upper()]
        except KeyError:
            pass  # Ignore non-scrabble letters
    return score


def max_word_value(word_list=None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    max_word = ""
    max_word_score = 0
    if word_list is None:
        word_list = load_words()
    # # Valid & Working:
    # for word in word_list:
    #     word_score = calc_word_value(word)
    #     if word_score > max_word_score:
    #         max_word = word
    #         max_word_score = word_score
    d = {calc_word_value(word): word for word in word_list}
    max_word = d[max(d.keys())]
    return max_word

if __name__ == "__main__":
    pass  # run unittests to validate
