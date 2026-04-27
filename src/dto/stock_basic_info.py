from dataclasses import dataclass

@dataclass(frozen=True)
class StockBasicInfo():
    # 股票 Code
    dm: str
    # 股票名称
    mc: str
    # 交易所
    jys: str