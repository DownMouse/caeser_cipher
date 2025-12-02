#описание работы шифра

def cipher(text: str, key: int, mode: str = 'encrypt') -> str:
    rus_lower = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    rus_upper = rus_lower.upper()

    eng_lower = "abcdefghijklmnopqrstuvwxyz"
    eng_upper = eng_lower.upper()

    #проверка корректоности режима
    if mode not in ('encrypt', 'decrypt'):
        raise ValueError('режим должен быть "зашифровать" или "дешифровать"')

    #дешифрование = отрицательный ключ
    if mode == 'decrypt':
        key = -key

    result = ''

    #проверяем каждый символ введенной строки
    for char in text:
        # Русские строчные
        if char in rus_lower:
            idx = rus_lower.index(char)
            result += rus_lower[(idx + key) % len(rus_lower)]

        # Русские заглавные
        elif char in rus_upper:
            idx = rus_upper.index(char)
            result += rus_upper[(idx + key) % len(rus_upper)]

        # Английские строчные
        elif char in eng_lower:
            idx = eng_lower.index(char)
            result += eng_lower[(idx + key) % len(eng_lower)]

        # Английские заглавные
        elif char in eng_upper:
            idx = eng_upper.index(char)
            result += eng_upper[(idx + key) % len(eng_upper)]

        #символы вне алфавита не меняем
        else:
            result += char

    return ''.join(result)