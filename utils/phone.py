import re


def normalize_phone(phone):
    if not phone:
        return None

    normalized = re.sub(r"\D", "", str(phone))
    return normalized or None


def is_valid_phone(phone):
    if not phone:
        return False

    return 12 <= len(phone) <= 13