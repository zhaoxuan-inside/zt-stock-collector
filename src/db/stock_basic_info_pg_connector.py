from .pg_connector import PGConnector

CREATE_TABLE = """
CREATE TABLE IF NOT EXISTS stock_basic_info (
    id UUID PRIMARY KEY,
    code CHAR(6) NOT NULL,
    name VARCHAR(4) NOT NULL,
    exchanger VARCHAR(2) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP DEFAULT NOW()
);

CREATE INDEX IF NOT EXIST idx_code ON stock_basic_info (code);
"""

class StockBasicInfoConnector(PGConnector):

    def __init__(self, dsn: str):
        super().__init__(dsn, "stock_basic_info", CREATE_TABLE)
        super().init_tables()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
