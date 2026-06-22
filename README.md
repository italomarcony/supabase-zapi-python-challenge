# Supabase Z-API Python Challenge

Projeto em Python para ler contatos do Supabase e enviar mensagens personalizadas via Z-API.

## Estrutura da tabela no Supabase

Tabela sugerida: `contacts`

Campos mínimos:
- `name` (text)
- `phone` (text)

## Variáveis de ambiente

Copie o arquivo `.env.example` para `.env` e preencha:

- `SUPABASE_URL`
- `SUPABASE_KEY`
- `SUPABASE_TABLE`
- `ZAPI_BASE_URL`
- `ZAPI_INSTANCE_ID`
- `ZAPI_TOKEN`
- `ZAPI_CLIENT_TOKEN`

## Como rodar

```bash
python main.py
```