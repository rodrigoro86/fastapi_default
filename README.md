# Modelo FastAPI com Docker

Este é um projeto simples utilizando FastAPI configurado para rodar em containers Docker usando Docker Compose. Esta configuração inclui um serviço web FastAPI.

## Índice

- [Começando](#começando)
- [Pré-requisitos](#pré-requisitos)
- [Instalação](#instalação)
- [Uso](#uso)
- [Documentação](#documentação)

## Começando

Siga estas instruções para configurar o projeto na sua máquina local.

### Pré-requisitos

Antes de começar, certifique-se de ter os seguintes itens instalados:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Instalação

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/seu-usuario/seu-repo.git
   cd seu-repo
   ```

2. **Construa e inicie os containers:**

   ```bash
   docker-compose up --build
   ```

   Este comando irá construir a imagem Docker para a aplicação FastAPI e iniciar os containers definidos no arquivo `docker-compose.yml`.

3. **Acesse a aplicação FastAPI:**

   Abra o navegador e navegue até `http://localhost:8000`.

4. **Acesse a documentação do FastAPI:**

   A documentação interativa da API está disponível em `http://localhost:8000/docs`.

### Uso

- Para parar os containers, use:

  ```bash
  docker-compose down
  ```

- Para reconstruir os containers após fazer alterações no código, use:

  ```bash
  docker-compose up --build
  ```

### Documentação
A aplicação FastAPI oferece duas opções de documentação interativa da API:

- **Swagger UI**: disponível em http://localhost:8000/docs  
- **ReDoc**: disponível em http://localhost:8000/redoc  
Ambas as interfaces fornecem uma visão geral detalhada dos endpoints disponíveis, bem como exemplos de requisições e respostas.
