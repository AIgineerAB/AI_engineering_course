from fastapi import FastAPI, Query
from data_processing import library_data, Book
from pprint import pprint
from constants import CURRENT_YEAR

app = FastAPI()


library = library_data("library.json")
books = library.books
pprint(books)


@app.get("/books")
async def read_books():
    return books


# path parameter - before query params
@app.get("/books/title/{title}")
async def read_book_by_title(title: str):
    return [book for book in books if book.title.casefold() == title.casefold()]


# query parameter - ?start_year=1950
@app.get("/books/")
async def filter_books(
    start_year: int = Query(
        1950,
        gt=1500,
        lt=CURRENT_YEAR + 1,
        description="Filters books that are newer than this year",
    ),
    author: str = Query(None, description="Authors firstname and lastname "),
):
    filtered_books = [book for book in books if start_year < book.year]

    if author:
        filtered_books = [
            book
            for book in filtered_books
            if author.casefold() == book.author.casefold()
        ]

    return filtered_books


@app.post("/books/create_book")
async def create_book(book_request: Book):
    new_book = Book.model_validate(book_request)
    books.append(new_book)

    return new_book

@app.put("/books/update_book")
async def update_book(updated_book: Book):
    for i, book in enumerate(books):
        if book.id == updated_book.id:
            books[i] = updated_book
    return updated_book

@app.delete("/books/delete_book/{id}")
async def delete_book(id: int):
    for i, book in enumerate(books):
        if book.id == id:
            del books[i]
            break