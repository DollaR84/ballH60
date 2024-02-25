LETTER_EN = 'abcdefghijklmnopqrstuvwxyz'
LETTER_RU = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'


REN = {l: i for i, l in enumerate(LETTER_EN, 1)}
REN.update({l: i for i, l in enumerate(LETTER_EN.upper(), 1)})
REN.update({l: i for i, l in enumerate(LETTER_RU, 1)})
REN.update({l: i for i, l in enumerate(LETTER_RU.upper(), 1)})
REN.update({str(i): i for i in range(10)})


def fix_num(number, base):
    """Return fix digit from number."""
    result = number % base
    if 0 == result:
        result = base
    return result


def sum_digits(digits, base):
    """Calc all digits in digits list."""
    if 1 == len(digits):
        return digits[0]
    else:
        return sum_digits([fix_num((digits[i]+digits[i+1]), base) for i in range(len(digits)-1)], base)


def calc(phrase, base, num_digits=False):
    """Calc symbols in phrase with 9 limit digits."""
    digits = []
    phrase = phrase.replace('\n', ' ')
    for word in phrase.split(' '):
        if '' == word:
            continue
        if num_digits:
            try:
                number = int(word)
            except:
                symbols = [s for s in word if s.isalnum()]
                digits.append(len(symbols))
            else:
                digits.append(number)
        else:
            symbols = [s for s in word if s.isalnum()]
            digits.append(len(symbols))
    return sum_digits(digits, base)
