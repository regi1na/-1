# TODO Найдите количество книг, которое можно разместить на дискете
pages_in_book = 100
strings_on_page = 50
memory_mb = 1.44
charactes_in_string = 25
one_character = 4

memory_bytes = memory_mb * 1024 * 1024
one_book_bytes = pages_in_book * strings_on_page * charactes_in_string * one_character
number_of_books = memory_bytes // one_book_bytes
print("Количество книг, помещающихся на дискету:", int(number_of_books))
