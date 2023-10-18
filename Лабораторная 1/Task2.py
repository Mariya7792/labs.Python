space_on_disk = 1.44
pages = 100
line_on_one_page = 50
symbols_on_line = 25
one_symbol_space = 4

space_for_one_book = one_symbol_space * symbols_on_line * line_on_one_page * pages
space_on_disk *= 1024 * 1024
books_on_disk = round(space_on_disk / space_for_one_book)
print("Количество книг, помещающихся на дискету:", books_on_disk)
