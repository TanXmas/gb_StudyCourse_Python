"""
Создать НЕ программно (вручную) текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».

Принудительно программно открыть файл в формате Unicode и вывести его содержимое.
Это значит, что при чтении файла вы должны явно указать кодировку utf-8
и файл должен открыться у ЛЮБОГО!!! человека при запуске вашего скрипта.

При сдаче задания в папке должен лежать текстовый файл!

Это значит вы должны предусмотреть случай, что вы по дефолту записали файл в cp1251, а прочитать пытаетесь в utf-8.

Подсказки:
--- обратите внимание, что заполнять файл вы можете в любой кодировке, но открыть нужно в формате Unicode (utf-8)
--- обратите внимание на чтение файла в режиме rb для последующей переконвертации в нужную кодировку
"""
from chardet import detect


def encoding_convert(file_name):
    with open(file_name, 'rb') as file:
        content_bytes = file.read()
    encoding = detect(content_bytes)['encoding']
    content_txt = content_bytes.decode(encoding)
    with open(file_name, 'w', encoding='utf8') as file:
        file.write(content_txt)


file_name = 'test_file.txt'
encoding_convert(file_name)
with open(file_name, 'r', encoding='utf8') as file:
    print(file.read())
