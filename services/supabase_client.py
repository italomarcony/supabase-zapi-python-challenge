import os

from supabase import create_client

from utils.logger import setup_logger


logger = setup_logger()


def get_supabase_client():
    """Cria e retorna uma instância do cliente Supabase."""

    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")

    return create_client(supabase_url, supabase_key)


def fetch_contacts(limit=3):
    """Busca contatos na tabela configurada no Supabase.

    Por padrão, retorna no máximo 3 contatos para respeitar a regra do desafio.
    """

    table_name = os.getenv("SUPABASE_TABLE", "contacts")

    try:
        logger.info("Buscando contatos na tabela '%s'...", table_name)

        client = get_supabase_client()

        response = (
            client.table(table_name)
            .select("id, name, phone")
            # Ordena pelo id para manter previsibilidade nos contatos retornados.
            .order("id")
            # Limita o resultado a até 3 registros, conforme exigido no desafio.
            .limit(limit)
            .execute()
        )

        contacts = response.data or []

        logger.info("Total de contatos retornados: %s", len(contacts))
        return contacts

    except Exception as error:
        logger.error("Erro ao buscar contatos no Supabase: %s", error)
        raise