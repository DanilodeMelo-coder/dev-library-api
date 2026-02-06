# 📚 Dev Library API

API REST desenvolvida com **FastAPI** para gerenciamento e recomendação de livros técnicos de desenvolvimento de software.

Este projeto foi desenvolvido durante um curso introdutório de FastAPI (Udemy) e **evoluído com melhorias próprias**, servindo como **projeto de estudo e portfólio**.

---

## 🚀 Funcionalidades

* 📄 Listar todos os livros cadastrados
* 🔍 Buscar livro pelo índice
* 🎲 Recomendar um livro aleatório
* ➕ Adicionar novos livros
* 💾 Persistência de dados em arquivo JSON
* ✅ Validação de dados com Pydantic
* 🆔 Identificação única dos livros com UUID

---

## 🛠️ Tecnologias utilizadas

* Python 3.10+
* FastAPI
* Pydantic
* UUID
* JSON (persistência local)

---

## 📦 Estrutura do projeto

```bash
dev-library-api/
│
├── main.py          # Arquivo principal da API
├── books.json       # Base de dados em JSON
├── README.md        # Documentação do projeto
```

---

## ▶️ Como executar o projeto

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/seu-usuario/dev-library-api.git
cd dev-library-api
```

### 2️⃣ Criar ambiente virtual (opcional, recomendado)

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3️⃣ Instalar dependências

```bash
pip install fastapi uvicorn
```

### 4️⃣ Executar a aplicação

```bash
uvicorn main:app --reload
```

A API estará disponível em:

```
http://127.0.0.1:8000
```

Documentação automática:

* Swagger UI → `http://127.0.0.1:8000/docs`
* Redoc → `http://127.0.0.1:8000/redoc`

---

## 📌 Endpoints disponíveis

### 🔹 Home

```http
GET /
```

### 🔹 Listar livros

```http
GET /list-books
```

### 🔹 Buscar livro por índice

```http
GET /list-books-by-index/{index}
```

### 🔹 Livro aleatório

```http
GET /random-book
```

### 🔹 Adicionar livro

```http
POST /add-book
```

Exemplo de corpo da requisição:

```json
{
  "name": "Código Limpo",
  "price": 79.90,
  "genre": "Teoria"
}
```

---

## 🧠 Aprendizados com o projeto

* Criação de APIs REST com FastAPI
* Uso de Pydantic para validação de dados
* Persistência simples sem banco de dados
* Tratamento de erros HTTP
* Organização de código para portfólio

---

## 🔮 Próximas melhorias planejadas

* ✏️ Atualizar livros
* 🗑️ Remover livros
* 🔐 Autenticação (admin / usuário)
* 🧪 Testes automatizados
* 🗄️ Integração com banco de dados

---

## 👨‍💻 Autor

**Danilo de Melo**
Estudante de Análise e Desenvolvimento de Sistemas
Foco em Engenharia de Software

---

📌 *Este projeto faz parte do meu portfólio e está em constante evolução.*
