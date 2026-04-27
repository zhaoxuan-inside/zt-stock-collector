from dataclasses import dataclass
from uuid6 import uuid7

# https://api.zhituapi.com/hs/history/股票代码.市场（如000001.SZ）/分时级别(如d)/除权方式?token=token证书&st=开始时间(如20240601)&et=结束时间(如20250430)

# t	string	交易时间
# o	float	开盘价
# h	float	最高价
# l	float	最低价
# c	float	收盘价
# v	float	成交量
# a	float	成交额
# pc	float	前收盘价
# sf	int	停牌 1停牌，0 不停牌
@dataclass
class StockExchangeDailyEntity():

    def __init__(self, t: str, o: float, h: float, l: float, c: float, v: float, a:float, pc: float, sf: int, code: str = ""):
        self.code = code
        self.t = t
        self.o = o
        self.h = h
        self.l = l
        self.c = c
        self.v = v
        self.a = a
        self.pc = pc
        self.sf = sf
        self.id: str = str(uuid7())
