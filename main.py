from fastapi import FastAPI, HTTPException
import random
import json
import os

app = FastAPI()

BOOKS_FILES = "books.json"

books_database= [
    "Clean Code",
    "O Programador Pragmático",
    "Código Limpo em Python",
    "Arquitetura Limpa",
    "Padrões de Projeto",
    "Algoritmos: Teoria e Prática"
]

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
async def add_book(book: str):
    books_database.append(book)

#pega tudo que esta na database e joga no arquivo "f"
    with open (BOOKS_FILES, "w") as f:                 #"w" -> whrite
        json.dump(books_database, f)

    return {"menssage": f"The book {book} was added with sucess"}