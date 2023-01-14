#Код Морзе для представления цифр и букв использует тире и точки.
#Напишите функцию для кодирования текстового сообщения в соответствии с кодом Морзе
text1 = input('Write a text: ')
def text_to_morse(text1):
    dict_morse = {
        'a': '.-',
        'b': '-...',
        'c': '-.-.',
        'd': '-..',
        'e': '.',
        'f': '..-.',
        'g': '--.',
        'h': '....',
        'i': '..',
        'j': '.---',
        'k': '-.-',
        'l': '.-..',
        'm': '--',
        'n': '-.',
        'o': '---',
        'p': '.--.',
        'q': '--.-',
        'r': '.-.',
        's': '...',
        't': '-',
        'u': '..-',
        'v': '...-',
        'w': '.--',
        'x': '-..-',
        'y': '-.--',
        'z': '--..',
        '1': '.---',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        '0': '-----',
        ' ': ' '
    }

    text1 = text1.lower()
    result1 = ''
    for i in text1:
        result1 += dict_morse.get(i, '')
        if i in dict_morse:
            result1 += ' '
    print(result1)

text_to_morse(text1)
