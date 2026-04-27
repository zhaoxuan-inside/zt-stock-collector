from dataclasses import dataclass
from uuid6 import uuid7

@dataclass
class StockExchangeInfoEntity():

    def __init__(self, code: str, date: str, time: str, value: int, price: int, order: int):
        self.code = code
        self.datetime = date + " " + time
        self.value = self.value
        self.order = order

    id: str = str(uuid7())