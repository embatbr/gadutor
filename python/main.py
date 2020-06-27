# -*- coding: utf-8 -*-

VOWELS = 'AÁÀÃÂEÉÈẼÊIÍÌĨÎOÓÒÕÔUÚÙŨÛ'
CONSONANTS = 'BCÇDFGHJKLMNPQRSTVWXYZ'
ALPHABET = f'{VOWELS}{CONSONANTS}'

MU_FACTOR = 3


def return_symbols(mu_word, word, size, num_vowels, num_consonants):
    if size > (num_vowels + num_consonants):
        left = 0
        right = size - 1
        search_left = search_right = True
        while (left < right) and (search_left or search_right):
            if word[left].upper() not in ALPHABET:
                left = left + 1
            else:
                search_left = False

            if word[right].upper() in ALPHABET:
                search_right = False
            else:
                right = right - 1

        word_left = word[:left]
        word_right = word[right+1:]

        return '{}{}{}'.format(word_left, mu_word, word_right)

    return mu_word


def gadizate_word(word):
    size = len(word)
    num_vowels = len([w for w in word if w.upper() in VOWELS])
    num_consonants = len([w for w in word if w.upper() in CONSONANTS])

    if (size > 1) and (word[0] in '@#'):
        return word

    if num_vowels == num_consonants == 0:
        return word

    mu_word = 'mu'
    if num_vowels > num_consonants:
        mu_word = '{}u'.format(mu_word)

    factor = max(size // MU_FACTOR, 1)
    mu_word = mu_word * factor

    if word.isupper():
        mu_word = mu_word.upper()
    elif word[0].isupper():
        mu_word = '{}{}'.format(mu_word[0].upper(), mu_word[1:])

    mu_word = return_symbols(mu_word, word, size, num_vowels, num_consonants)

    return mu_word


def gadizate_words(words):
    mu_words = list()

    for word in words:
        mu_word = gadizate_word(word.strip())
        mu_words.append(mu_word)

    return mu_words


def gadizate_sentence(sentence):
    words = sentence.split(' ')
    mu_words = gadizate_words(words)
    mu_sentence = ' '.join(mu_words)

    return mu_sentence


if __name__ == '__main__':
    sentence = input('> ').strip()
    mu_sentence = gadizate_sentence(sentence)

    print(mu_sentence)
