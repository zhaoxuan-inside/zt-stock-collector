from dataclasses import dataclass
from uuid6 import uuid7

@dataclass
class StockBasicInfoEntity():

    def __init__(self, code: str, name: str, exchanger: str):
        self.code = code
        self.name = name
        self.exchanger = exchanger

    id: str = str(uuid7())