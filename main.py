import os
import sys

from dotenv import load_dotenv

from services.supabase_client import fetch_contacts
from utils.logger import setup_logger


REQUIRED_ENV_VARS = [
    "SUPABASE_URL",
    "SUPABASE_KEY",
    "SUPABASE_TABLE",
    "ZAPI_INSTANCE_ID",
    "ZAPI_TOKEN",
    "ZAPI_CLIENT_TOKEN",
    "ZAPI_BASE_URL",
]


def validate_env_vars():
    missing_vars = [var for var in REQUIRED_ENV_VARS if not os.getenv(var)]
    return missing_vars


def main():
    load_dotenv()
    logger = setup_logger()

    logger.info("Iniciando aplicação...")

    missing_vars = validate_env_vars()

    if missing_vars:
        logger.error("Variáveis de ambiente ausentes: %s", ", ".join(missing_vars))
        sys.exit(1)

    logger.info("Variáveis de ambiente carregadas com sucesso.")

    try:
        contacts = fetch_contacts(limit=3) 

        if not contacts:
            logger.warning("Nenhum contato encontrado na tabela.")
            return

        logger.info("Contatos encontrados com sucesso:")

        for index, contact in enumerate(contacts, start=1):
            logger.info(
                "%s. Nome: %s | Telefone: %s",
                index,
                contact.get("name"),
                contact.get("phone"),
            )

    except Exception:
        logger.error("Falha na execução do fluxo de leitura do Supabase.")
        sys.exit(1)


if __name__ == "__main__":
    main()