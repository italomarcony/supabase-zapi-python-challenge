import os
import sys

from dotenv import load_dotenv

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
        logger.error(
            "Variáveis de ambiente ausentes: %s",
            ", ".join(missing_vars)
        )
        sys.exit(1)

    logger.info("Variáveis de ambiente carregadas com sucesso.")
    logger.info("Estrutura base validada. Pronto para integrar Supabase e Z-API.")


if __name__ == "__main__":
    main()