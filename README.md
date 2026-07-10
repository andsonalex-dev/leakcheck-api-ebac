# Check My Email and Username API
Projeto EBAC
API simples em FastAPI para consultar dados na LeakCheck API.

## O que este projeto faz

- Endpoint de email: GET /api/v1/email/{email}
- Endpoint de username: GET /api/v1/username/{username}
- Endpoint de saude: GET /health
- Configuracao via arquivo .env
- Execucao com Docker e Docker Compose
- Dependencias gerenciadas com Poetry

## Requisitos

- Docker
- Docker Compose

## Variaveis de ambiente

Use o arquivo .env com os campos abaixo:

    APP_NAME=LeakCheck API
    APP_ENV=development
    HOST=0.0.0.0
    PORT=8000
    LEAKCHECK_URL=https://leakcheck.io/api/public

## Subir o projeto

Na raiz do projeto:

    docker compose up --build -d

Ver status:

    docker compose ps

Ver logs:

    docker compose logs -f api

Parar:

    docker compose down

## Testar endpoints

Health:

    curl http://localhost:8000/health

Email:

    curl "http://localhost:8000/api/v1/email/test@example.com"

Username:

    curl "http://localhost:8000/api/v1/username/john"

## Execucao local sem Docker (opcional)

Instalar dependencias com Poetry:

    poetry install

Rodar a API:

    poetry run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

## Estrutura principal

- app/main.py: inicializacao do FastAPI
- app/api/router.py: roteador principal
- app/api/routes/email.py: rota de email
- app/api/routes/name.py: rota de username
- app/api/routes/health.py: rota de saude
- app/services/leakcheck_service.py: regra de negocio
- app/clients/leakcheck_client.py: cliente HTTP para LeakCheck
- app/core/config.py: leitura das variaveis de ambiente
