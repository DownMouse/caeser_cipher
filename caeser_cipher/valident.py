def v_key(key_str: str) -> int:
    #проверка на пустоту ключа
    if not key_str.strip():
        raise ValueError("ключ не может быть пустым")

    #проверка ключа на число
    if not key_str.lstrip('-').isdigit():
        raise ValueError("ключ должен быть числом")

    return int(key_str)
