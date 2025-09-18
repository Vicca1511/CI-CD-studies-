FROM python:3.11-slim

WORKDIR /usr/src/app

# Define PYTHONPATH para incluir o diretório de trabalho
ENV PYTHONPATH=/usr/src/app

COPY requirements.txt requirements-dev.txt ./

RUN pip install --no-cache-dir \
    -r requirements.txt \
    -r requirements-dev.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]