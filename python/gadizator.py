# -*- coding: utf-8 -*-

VOWELS = 'AÁÀÃÂEÉÈẼÊIÍÌĨÎOÓÒÕÔUÚÙŨÛ'
CONSONANTS = 'BCÇDFGHJKLMNPQRSTVWXYZ'
ALPHABET = f'{VOWELS}{CONSONANTS}'

MU_FACTOR = 3


def return_symbols(simple_mu_word, simple_word, size, num_vowels, num_consonants):
    if size > (num_vowels + num_consonants):
        left = 0
        right = size - 1
        search_left = search_right = True
        while (left < right) and (search_left or search_right):
            if simple_word[left].upper() not in ALPHABET:
                left = left + 1
            else:
                search_left = False

            if simple_word[right].upper() in ALPHABET:
                search_right = False
            else:
                right = right - 1

        word_left = simple_word[:left]
        word_right = simple_word[right+1:]

        return '{}{}{}'.format(word_left, simple_mu_word, word_right)

    return simple_mu_word


def gadizate_simple_world(simple_word):
    size = len(simple_word)
    num_vowels = len([w for w in simple_word if w.upper() in VOWELS])
    num_consonants = len([w for w in simple_word if w.upper() in CONSONANTS])

    simple_mu_word = 'mu'
    if num_vowels > num_consonants:
        simple_mu_word = '{}u'.format(simple_mu_word)

    factor = max(size // MU_FACTOR, 1)
    simple_mu_word = simple_mu_word * factor

    if simple_word.isupper():
        simple_mu_word = simple_mu_word.upper()
    elif simple_word[0].isupper():
        simple_mu_word = '{}{}'.format(simple_mu_word[0].upper(), simple_mu_word[1:])

    simple_mu_word = return_symbols(simple_mu_word, simple_word, size, num_vowels, num_consonants)

    return simple_mu_word


def gadizate_word(word):
    size = len(word)
    num_vowels = len([w for w in word if w.upper() in VOWELS])
    num_consonants = len([w for w in word if w.upper() in CONSONANTS])

    if (size > 1) and (word[0] in '@#'):
        return word

    if num_vowels == num_consonants == 0:
        return word

    simple_words = word.split('-')
    mu_word = list()

    for simple_word in simple_words:
        simple_word = simple_word.strip()
        if simple_word:
            simple_mu_word = gadizate_simple_world(simple_word.strip())
            mu_word.append(simple_mu_word)

    mu_word = '-'.join(mu_word)

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
    with open('input.txt') as infile:
        mu_sentences = list()

        for sentence in infile.readlines():
            mu_sentence = gadizate_sentence(sentence)
            mu_sentences.append(mu_sentence)

        mu_sentences = '\n'.join(mu_sentences)
        with open('output.txt', 'w') as outfile:
            outfile.write(mu_sentences)