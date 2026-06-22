import os

import requests

from utils.logger import setup_logger


logger = setup_logger()


def build_zapi_url():
    """Monta a URL do endpoint de envio de texto da Z-API."""

    base_url = os.getenv("ZAPI_BASE_URL")
    instance_id = os.getenv("ZAPI_INSTANCE_ID")
    token = os.getenv("ZAPI_TOKEN")

    return f"{base_url}/instances/{instance_id}/token/{token}/send-text"


def send_text_message(phone, message):
    """Envia uma mensagem de texto simples para um telefone via Z-API."""

    url = build_zapi_url()
    client_token = os.getenv("ZAPI_CLIENT_TOKEN")

    headers = {
        # O Client-Token é enviado no header para autenticar a requisição.
        "Client-Token": client_token,
        "Content-Type": "application/json",
    }

    payload = {
        "phone": phone,
        "message": message,
    }

    try:
        logger.info("Enviando mensagem para %s...", phone)

        response = requests.post(
            url,
            json=payload,
            headers=headers,
            # Define timeout para evitar que a aplicação fique travada indefinidamente.
            timeout=30,
        )

        # Lança exceção caso a API retorne erro HTTP (4xx ou 5xx).
        response.raise_for_status()

        logger.info("Mensagem enviada com sucesso para %s.", phone)
        return response.json()

    except requests.exceptions.RequestException as error:
        logger.error("Erro ao enviar mensagem para %s: %s", phone, error)
        raise