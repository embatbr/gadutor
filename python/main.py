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
    'T', 'V', 'W', 'X', 'Y', 'Z',
    'Ç'
)


def gadizate_word(word):
    mu_word = list()

    last_mu_letter = ''
    had_symbol_last_time = False

    size = len(word)
    for i in range(size):
        letter = word[i]

        mu_letter = letter

        if letter in VOWELS:
            mu_letter = 'U'
            had_symbol_last_time = False

        elif letter in CONSONANTS:
            if last_mu_letter == 'M':
                mu_letter = 'U'
            elif i == (size - 1):
                mu_letter = 'MÚ'
            else:
                mu_letter = 'M'

            had_symbol_last_time = False

        elif letter in ('.', ',', ':', ';', '!', '?'):
            if not had_symbol_last_time:
                mu_letter = 'UH{}'.format(letter)
                had_symbol_last_time = True

        else:
            mu_letter = 'MUH'
            had_symbol_last_time = False

        last_mu_letter = mu_letter

        mu_word.append(mu_letter)

    if mu_word:
        if mu_word[0] == 'U':
            mu_word.insert(0, 'M')
        elif mu_word[-1] == 'M':
            mu_word.append('U')

    if (len(mu_word) > 2) and (mu_word[-1] == mu_word[-2] == 'U'):
        mu_word[-1] = 'UH'

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


if __name__ == '__main__':
    sentence = input('> ').strip()

    mu_sentence = gadizate_sentence(sentence)
    print(mu_sentence)
