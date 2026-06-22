import logging


def setup_logger():
    """Configura e retorna o logger principal da aplicação."""

    # basicConfig é suficiente para este projeto porque queremos um log simples,
    # legível no terminal e configurado em um único lugar.
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    return logging.getLogger("supabase_zapi_app")