# Usar uma imagem base do Python
FROM python:3.11-slim

# Definir o diretório de trabalho no container
WORKDIR /app

# Copiar os arquivos de requisitos para o container
COPY requirements.txt .

# Instalar as dependências necessárias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código da aplicação para o container
COPY . .

# Expor a porta em que o FastAPI irá rodar
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["python", "app.py"]
