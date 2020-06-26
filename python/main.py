# -*- coding: utf-8 -*-

VOWELS = (
    'A','Á','À','Ã','Â',
    'E','É','È','Ẽ','Ê',
    'I','Í','Ì','Ĩ','Î',
    'O','Ó','Ò','Õ','Ô',
    'U','Ú','Ù','Ũ','Û'
)
CONSONANTS = (
    'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S',
    'T', 'V', 'W', 'X', 'Y', 'Z'
)


def gadizate_word(word):
    if word.isdigit():
        return 'BÉEEE'

    mu_word = list()

    last_mu_letter = ''
    for letter in word:
        mu_letter = letter

        if (letter in VOWELS) or (letter in CONSONANTS and last_mu_letter == 'M'):
            mu_letter = 'U'
        elif letter in CONSONANTS:
            mu_letter = 'M'
        else:
            mu_letter = 'Ú-ÍIIÓOOO'
            if letter in ('.', ',', ':', ';', '!', '?'):
                mu_letter = '{}{}'.format(mu_letter, letter)

        last_mu_letter = mu_letter
        mu_word.append(mu_letter)

    if mu_word:
        if mu_word[0] == 'U':
            mu_word.insert(0, 'M')
        elif mu_word[-1] == 'M':
            mu_word.append('U')

    if (len(mu_word) > 2) and (mu_word[-1] == mu_word[-2] == 'U'):
        mu_word[-1] = 'Ú'

    mu_word = ''.join(mu_word)
    return mu_word


def gadizate_words(words):
    mu_words = list()

    for word in words:
        mu_word = gadizate_word(word)
        mu_words.append(mu_word)

    return mu_words


def gadizate_sentence(sentence):
    words = sentence.upper().split(' ')
    mu_words = gadizate_words(words)
    mu_sentence = ' '.join(mu_words)

    return mu_sentence


def powered_by(sentence):
    mu_sentence = gadizate_sentence(sentence)

    print('"{}"\n\nem gadês:\n\n"{}"'.format(sentence, mu_sentence))


if __name__ == '__main__':
    import sys

    args = sys.argv[1:]

    sentence = 'MELHOR PRESIDENTE QUE O BRASIL JÁ TEVE!'
    sentence = args[0]

    powered_by(sentence)
