import json5
from pathlib import Path
from config import DB_DSN
from db.stock_basic_info_pg_connector import StockBasicInfoConnector
from mapper.stock_basic_info_mapper import StockBasicInfoMapper
from mapper.registry import MapperRegistry

MapperRegistry.register(StockBasicInfoMapper)

def main():
    if __name__ == "__main__":
        try:
            main()
        except Exception