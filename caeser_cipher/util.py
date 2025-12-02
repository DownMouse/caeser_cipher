def load_file(path: str) -> str:

    try: #открываем файл в ютф8
        with open(path, "r", encoding="utf-8") as f:
            return f.read()

    except UnicodeDecodeError: #в случае провала, открываем в сп1251
        with open(path, "r", encoding="cp1251") as f:
            return f.read()

#сохраняем текст в виде файла
def text_file(path: str, text: str):
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)