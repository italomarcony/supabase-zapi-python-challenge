import os
import sys

from dotenv import load_dotenv

from services.supabase_client import fetch_contacts
from services.zapi_client import send_text_message
from utils.logger import setup_logger
from utils.phone import is_valid_phone, normalize_phone


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


def build_valid_contacts(raw_contacts, logger):
    valid_contacts = []

    for contact in raw_contacts:
        name = contact.get("name")
        raw_phone = contact.get("phone")

        normalized_phone = normalize_phone(raw_phone)

        if not normalized_phone:
            logger.warning("Contato '%s' ignorado: telefone ausente.", name)
            continue

        if not is_valid_phone(normalized_phone):
            logger.warning(
                "Contato '%s' ignorado: telefone inválido após normalização (%s).",
                name,
                normalized_phone,
            )
            continue

        valid_contacts.append(
            {
                "name": name,
                "phone": normalized_phone,
            }
        )

    return valid_contacts


def build_message(name):
    return f"Olá, {name} tudo bem com você?"


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
        raw_contacts = fetch_contacts(limit=3)

        if not raw_contacts:
            logger.warning("Nenhum contato encontrado na tabela.")
            return

        valid_contacts = build_valid_contacts(raw_contacts, logger)

        if not valid_contacts:
            logger.warning("Nenhum contato válido encontrado para envio.")
            return

        logger.info("Iniciando envio de mensagens para %s contato(s)...", len(valid_contacts))

        for contact in valid_contacts:
            message = build_message(contact["name"])
            send_text_message(contact["phone"], message)

        logger.info("Fluxo finalizado com sucesso.")

    except Exception:
        logger.error("Falha na execução do fluxo completo.")
        sys.exit(1)


if __name__ == "__main__":
    main()