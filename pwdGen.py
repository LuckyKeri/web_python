import hashlib

# основная функция 
def pwdGenerator(pwd_str: str, salt_str: str, num_char: str) -> str:
    # конкатенация строк
    pwd_str = pwd_str + salt_str
    # кодирование в байт-строку
    byte_str = pwd_str.encode()
    # хеширование 
    hash_str = hashlib.sha256(byte_str)
    # преобразование в обычную строку
    if not num_char.isnumeric():
        hex_str = hash_str.hexdigest()
    else:
        hex_str = hash_str.hexdigest()[:int(num_char)]
    # возврат хеш-строки
    return hex_str