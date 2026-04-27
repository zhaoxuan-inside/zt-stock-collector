from dataclasses import dataclass
from uuid6 import uuid7

@dataclass
class StockBasicInfoEntity():

    def __init__(self, dm: str, mc: str, jys: str):
        self.dm = dm
        self.mc = mc
        self.jys = jys
        self.id: str = str(uuid7())