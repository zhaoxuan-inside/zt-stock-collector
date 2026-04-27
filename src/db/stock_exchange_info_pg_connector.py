from .pg_connector import PGConnector

CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS {table_name} (
    id UUID PRIMARY KEY,
    datetime TIMESTAMP NOT NULL,
    value Integer NOT NULL,
    price Float NOT NULL,
    order VARCHAR(4) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX IF NOT EXIST idx_code ON stock_basic_info (code);
"""

class StockExchangeInfoConnector(PGConnector):

    def __init__(self, dsn: str, date: str):
        table_name: str = 'stock_exchange_info_' + date
        sql = CREATE_TABLE.replace("{table_name}", table_name)
        super().__init__(dsn, table_name, sql)
        super().init_tables()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
