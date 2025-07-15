# API de Empresas

Uma API REST desenvolvida com FastAPI para gerenciamento de empresas, permitindo operações CRUD (Create, Read, Update, Delete) completas.

## 📋 Funcionalidades

- ✅ Cadastrar novas empresas
- ✅ Listar todas as empresas
- ✅ Buscar empresa por ID
- ✅ Atualizar dados de empresas
- ✅ Excluir empresas
- ✅ Validação de CNPJ único
- ✅ Validação de dados de entrada

## 🛠️ Tecnologias Utilizadas

- **FastAPI** - Framework web moderno e rápido
- **SQLAlchemy** - ORM para banco de dados
- **Pydantic** - Validação de dados
- **SQLite** - Banco de dados local
- **Uvicorn** - Servidor ASGI

## 📦 Instalação

1. Clone o repositório:
```bash
git clone <url-do-repositorio>
cd empresa_api
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute a aplicação:
```bash
uvicorn main:app --reload
```

A API estará disponível em: `http://localhost:8000`

## 📚 Documentação da API

Após iniciar o servidor, acesse:
- **Swagger UI**: `http://localhost:8000/docs`
- **ReDoc**: `http://localhost:8000/redoc`

## 🔗 Endpoints

### Base URL: `http://localhost:8000`

| Método | Endpoint | Descrição |
|--------|----------|-----------|
| POST | `/enterprise/` | Criar nova empresa |
| GET | `/enterprise/` | Listar todas as empresas |
| GET | `/enterprise/{id}` | Buscar empresa por ID |
| PUT | `/enterprise/{id}` | Atualizar empresa |
| DELETE | `/enterprise/{id}` | Excluir empresa |

## 📝 Exemplos de Uso

### 1. Criar uma nova empresa

**POST** `/enterprise/`

```json
{
  "name": "Tech Solutions",
  "year_of_foundation": 2005,
  "cnpj": "12.345.678/0001-99",
  "telephone": "(11) 98765-4321",
  "social_value": 500000.00
}
```

**Resposta (201 Created):**
```json
{
  "id": 1,
  "name": "Tech Solutions",
  "year_of_foundation": 2005,
  "cnpj": "12.345.678/0001-99",
  "telephone": "(11) 98765-4321",
  "social_value": 500000.00
}
```

### 2. Listar todas as empresas

**GET** `/enterprise/`

**Resposta (200 OK):**
```json
[
  {
    "id": 1,
    "name": "Tech Solutions",
    "year_of_foundation": 2005,
    "cnpj": "12.345.678/0001-99",
    "telephone": "(11) 98765-4321",
    "social_value": 500000.00
  }
]
```

### 3. Buscar empresa por ID

**GET** `/enterprise/1`

**Resposta (200 OK):**
```json
{
  "id": 1,
  "name": "Tech Solutions",
  "year_of_foundation": 2005,
  "cnpj": "12.345.678/0001-99",
  "telephone": "(11) 98765-4321",
  "social_value": 500000.00
}
```

### 4. Atualizar empresa

**PUT** `/enterprise/1`

```json
{
  "name": "Tech Solutions Ltda",
  "year_of_foundation": 2005,
  "cnpj": "12.345.678/0001-99",
  "telephone": "(11) 99999-9999",
  "social_value": 750000.00
}
```

**Resposta (200 OK):**
```json
{
  "id": 1,
  "name": "Tech Solutions Ltda",
  "year_of_foundation": 2005,
  "cnpj": "12.345.678/0001-99",
  "telephone": "(11) 99999-9999",
  "social_value": 750000.00
}
```

### 5. Excluir empresa

**DELETE** `/enterprise/1`

**Resposta (204 No Content)**

## ⚠️ Códigos de Erro

| Código | Descrição |
|--------|-----------|
| 400 | CNPJ já cadastrado |
| 404 | Empresa não encontrada |
| 422 | Dados de entrada inválidos |

## 📋 Validações

- **Nome**: Obrigatório
- **Ano de fundação**: Entre 1800 e 2100
- **CNPJ**: 14-18 caracteres, único no sistema
- **Telefone**: 10-15 caracteres
- **Capital social**: Valor positivo

## 🗂️ Estrutura do Projeto

```
empresa_api/
├── app/
│   ├── database/
│   │   ├── __init__.py
│   │   └── connection.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── enterprise_model.py
│   ├── routers/
│   │   ├── __init__.py
│   │   └── enterprise.py
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── enterprise_schema.py
│   └── __init__.py
├── main.py
├── requirements.txt
├── enterprise.db
└── README.md
```

## 🚀 Testando com cURL

```bash
# Criar empresa
curl -X POST "http://localhost:8000/enterprise/" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Minha Empresa",
    "year_of_foundation": 2020,
    "cnpj": "11.222.333/0001-44",
    "telephone": "(11) 91234-5678",
    "social_value": 100000.00
  }'

# Listar empresas
curl -X GET "http://localhost:8000/enterprise/"

# Buscar por ID
curl -X GET "http://localhost:8000/enterprise/1"
```

## 📄 Licença

Este projeto está sob a licença MIT.