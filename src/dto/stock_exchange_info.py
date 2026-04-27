from dataclasses import dataclass

@dataclass(frozen=True)
class StockExchangeInfo():
    # 交易日期
    d: str
    # 交易时间
    t: str
    # 交易量
    v: int
    # 交易价格
    p: float
    # 交易方向
    ts: int