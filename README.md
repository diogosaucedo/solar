# Solar

Este projeto utiliza Docker Compose para gerenciar o ambiente de desenvolvimento com um front end e um back end. O front end está acessível na porta 8080 e o back end na porta 8001.

## Pré-requisitos

- [Docker](https://docs.docker.com/get-docker/) - Certifique-se de que o Docker está instalado em sua máquina.
- [Docker Compose](https://docs.docker.com/compose/install/) - O Docker Compose geralmente está incluído com o Docker Desktop.

## Estrutura do Projeto

```plaintext
Solar/
│
├── frontend/            # Código-fonte do front end (React)
│   ├── Dockerfile       # Dockerfile para o front end
│   └── ...              # Outros arquivos do front end
│
├── api/             # Código-fonte do back end (Django)
│   ├── Dockerfile       # Dockerfile para o back end
│   └── ...              # Outros arquivos do back end
│
└── docker-compose.yml   # Arquivo Docker Compose para orquestração dos containers
```

## Como executar

```shell
docker compose up
```
