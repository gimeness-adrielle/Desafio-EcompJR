# API de Gerenciamento de Empresas Clientes

Esta API permite gerenciar informações de empresas clientes da Ecomp JR., incluindo cadastro, consulta, atualização, exclusão e filtros avançados de busca.

---

## Tecnologias Utilizadas

- **FastAPI**: Framework web para construção da API
- **PostgreSQL**: Banco de dados relacional
- **SQLAlchemy**: ORM para manipulação do banco de dados
- **Pydantic**: Validação de dados e schemas

---

## Endpoints

### 1. CREATE - Criar empresa
**POST** `/empresas`

**Request Body (JSON)**
```json
{
    "nome": "Empresa da Paçoca",
    "cnpj": "12.345.678/0001-99",
    "cidade": "Feira de Santana",
    "ramo_atuacao": "Alimentos",
    "telefone": "(75) 99999-9999",
    "email_contato": "empresa@pacoca.com",
    "data_cadastro": "2025-09-25"
}
```

**Response**
```json
{
    "nome": "Empresa da Paçoca",
    "cnpj": "12.345.678/0001-99",
    "cidade": "Feira de Santana",
    "ramo_atuacao": "Alimentos",
    "telefone": "(75) 99999-9999",
    "email_contato": "empresa@pacoca.com",
    "data_cadastro": "2025-09-25"
}
```

**Erros**
- **400**: CNPJ ou email já cadastrado.

### 2. READ - Listar empresas
**GET** `/empresas`

**Query Parameters (opcionais)**
- **cidade**: Filtra empresas por cidade
- **ramo_atuacao**: Filtra empresas pelo ramo de atuação
- **nome**: Busca pelo nome da empresa

-> Exemplo: 
    `/empresas?cidade=Feira de Santana&ramo_atuacao=Alimentos&nome=Paçoca`

**Response**
```json
[
  {
    "id": 1,
    "nome": "Empresa Da Paçoca",
    "cnpj": "12.345.678/0001-99",
    "cidade": "Feira de Santana",
    "ramo_atuacao": "Alimentos",
    "telefone": "(75) 99999-9999",
    "email_contato": "empresa@pacoca.com",
    "data_cadastro": "2025-09-25"
  }
]
```

### 3. READ - Buscar detalhes de uma empresa pelo ID
**GET** `/empresas/{empresa_id}`

**Response**
```json
[
  {
    "id": 1,
    "nome": "Empresa Da Paçoca",
    "cnpj": "12.345.678/0001-99",
    "cidade": "Feira de Santana",
    "ramo_atuacao": "Alimentos",
    "telefone": "(75) 99999-9999",
    "email_contato": "empresa@pacoca.com",
    "data_cadastro": "2025-09-25"
  }
]
```

**Erros**
- **404**: Empresa não encontrada.

### 4. UPDATE - Atualizar Empresa
**PUT** `/empresas/{empresa_id}`

**Request Body (JSON) - apenas campos que deseja alterar**

```json
{
  "telefone": "(75) 98888-8888",
  "cidade": "Salvador"
}
```

**Response**
```json
{
  "id": 1,
  "nome": "Empresa Da Paçoca",
  "cnpj": "12.345.678/0001-99",
  "cidade": "Salvador",
  "ramo_atuacao": "Alimentos",
  "telefone": "(75) 98888-7777",
  "email_contato": "empresa@pacoca.com",
  "data_cadastro": "2025-09-25"
}
```

**Erros**
- **404**: Empresa não encontrada
- **400**: CNPJ ou email duplicado

### 5. DELETE - Deletar Empresa
**DELETE** `/empresas/{empresa_id}`

**Response**
```json
{
  "detail": "Empresa deletada com sucesso!"
}
```

**Erros**
- **404**: Empresa não encontrada
