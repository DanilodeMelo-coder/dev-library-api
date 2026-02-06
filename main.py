from typing import Literal, Optional
from uuid import uuid4
from fastapi import FastAPI, HTTPException
import random
import json
import os
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

app = FastAPI()

class Book (BaseModel):
    name: str
    price: float
    book_id: Optional[str] = uuid4().hex
    genre: Literal["Melhorar-código", "Teoria"]


BOOKS_FILES = "books.json"

books_database = []


#checar se o caminho existe
if os.path.exists(BOOKS_FILES):          #Se o caminho do sistama operacional existir
    with open (BOOKS_FILES, 'r') as f: #"r" -> read 
        books_database = json.load(f) 



#/ -> Boas vindas
@app.get("/")
async def home():
    return "Welcome to the dev'library "


#/list-books -> listar todos os livros
@app.get("/list-books")
async def list_books():
    return { "books" : books_database}


#/list-books-by-index/{index} -> listar livro pelo index
@app.get("/list-books-by-index/{index}")
async def list_books_by_index(index: int):

    #se o index for menor que zero ou maior ou igual a len(books_database)
    if index < 0 or index >= len(books_database):
        #erro

        #raise → lança um erro
        #HTTPException → erro HTTP controlado
        raise HTTPException (404, "Index out of range")

    #caso ao contrario me retorne o livro pelo index
    else:
        return {"books": books_database[index] }


#/random-book -> recomendar livro aleatorio
@app.get("/random-book")
async def random_book():
    random_livro = random.choice(books_database)

    return f"book suggestion: {random_livro}"


#/add-book -> adicionar livro
@app.post("/add-book")
async def add_book(book: Book):
    book.book_id = uuid4().hex
    json_book = jsonable_encoder(book)
    books_database.append(json_book)

#pega tudo que esta na database e joga no arquivo "f"
    with open (BOOKS_FILES, "w") as f:                 #"w" -> whrite
        json.dump(books_database, f)

    return {"menssage": f"The book {book} was added with sucess"}

#/delete-book -> remover livro
@app.delete("/delete-book/{id}")
def delete_book(id):
    for index, book in enumerate(books_database):
        if book["book_id"] == id:
            books_database.pop(index)

            with open (BOOKS_FILES, 'w') as f:
                json.dump(books_database, f)

            return {"message": f"The book from id {id} has been removed"}
        
    raise HTTPException (404, "Id not found ")


#/update-book -> atualizar livro
@app.put("/update-book/{id}")
def update_book(id, book: Book):
    for index, book_db in enumerate(books_database):
        if book_db["book_id"] == id:
            book_update = {
                "name": book.name,
                "price": book.price,
                "book_id": id,
                "genre": book.genre
            }
            books_database[index] = book_update

            with open (BOOKS_FILES, "w") as f:
                json.dump(books_database, f)



            return {"message": f"The book from id {id} has been updated"}