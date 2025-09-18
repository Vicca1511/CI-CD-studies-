FROM python:3.11-slim

WORKDIR /usr/src/app

# Copia primeiro os requirements para aproveitar cache do Docker
COPY requirements.txt requirements-dev.txt ./

# Instala dependências base e dev (se existirem)
RUN pip install --no-cache-dir -r requirements.txt && \
    if [ -f requirements-dev.txt ]; then pip install -r requirements-dev.txt; fi

# Copia todo o código para o container
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]