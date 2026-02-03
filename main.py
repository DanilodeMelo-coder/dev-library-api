from fastapi import FastAPI

app = FastAPI()

books_database= [
    "Clean Code",
    "O Programador Pragmático",
    "Código Limpo em Python",
    "Arquitetura Limpa",
    "Padrões de Projeto",
    "Algoritmos: Teoria e Prática"
]


#/ -> Boas vindas
@app.get("/")
async def home():
    return "Welcome to the programmers'library "


#/list-books -> listar todos os livros
@app.get("/list-books")
async def list_books():
    return { "books" : books_database}


#/list-books-by-index/{index} -> listar livro pelo index
@app.get("/list-books-by-index/{index}")
async def list_books_by_index(index: int):

    return {"books": books_database[index] }
    


#/random-list -> recomendar livro aleatorio
#/add-book -> adicionar livro