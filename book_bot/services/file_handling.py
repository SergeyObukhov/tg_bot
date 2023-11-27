import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}


# Функция, возвращающая строку с текстом страницы и ее размер
def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    punctuation = [',', '.', '!', ':', ';', '?']
    end = start+page_size
    while True:
        if (end >= len(text)) or (text[end] not in punctuation):
            break
        else:
            end -= 1
    
    cropped_text = text[start: end]
    
    last_char = 0
    for char in punctuation:
        index = cropped_text.rfind(char)
        if index > last_char:
            last_char = index
            
    result = cropped_text[:last_char+1]
    
    return result, len(result)


# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    dropping_chars = ' \n\t'
    page_num = 0
    start = 0
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    while start < len(text):
        page_num += 1
        page_text, page_len = _get_part_text(text, start, PAGE_SIZE)
        start += page_len
        book[page_num] = page_text.lstrip(dropping_chars)


# Вызов функции prepare_book для подготовки книги из текстового файла
prepare_book(os.path.join(sys.path[0], os.path.normpath(BOOK_PATH)))