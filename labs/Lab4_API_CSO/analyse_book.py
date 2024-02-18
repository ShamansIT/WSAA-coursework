from book_api_dao import getAllBooks

books = getAllBooks()
()
total = 0
count = 0
for book in books:
    total += book['Price']
    count += 1

print(f"Avarage of {count} books is {round(total/count,2)} Euro")
