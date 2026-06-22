import re


def normalize_phone(phone):
    """Remove qualquer caractere não numérico do telefone."""

    if not phone:
        return None

    normalized = re.sub(r"\D", "", str(phone))
    return normalized or None


def is_valid_phone(phone):
    """Valida se o telefone possui um tamanho aceitável para o desafio."""

    if not phone:
        return False

    # Regra simples para este case:
    # aceita números com DDI + DDD + telefone, normalmente entre 12 e 13 dígitos.
    return 12 <= len(phone) <= 13