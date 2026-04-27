from typing import Any, List
from .base import Mapper
from db.stock_exchange_daily_entity import StockExchangeDailyEntity

class StockExchangeInfoMapper(Mapper):

    def check_item(self, data: dict) -> bool:
        return "d" in data and "t" in data and "v" in data and "p" in data and "ts" in data

    def can_handle(self, data: Any) -> bool:
        if (isinstance(data, dict)):
            return self.check_item(data)
        if (isinstance(data, list)):
            for item in data:
                if (not isinstance(item, dict)):
                    return False;
                return self.check_item(item)
            return True
        return False
    
    def map(self, data: Any) -> List[StockExchangeDailyEntity]:
        match data:
            case dict():
                items = [data]
            case list():
                items = data
            case _:
                raise TypeError("invalid data type.")
            
        result = []

        for idx, raw in enumerate(items):
            t = raw.get("t")
            if (not isinstance(t, str) or not (t := t.strip())):
                raise ValueError(f"t invalid. idx: {idx}, field: d. content: {t}")
            
            o = raw.get("o")
            if (not isinstance(o, float) or not (o > 0.00)):
                raise ValueError(f"o invalid. idx: {idx}, field: t. content: {o}")
            
            h = raw.get("h")
            if (not isinstance(h, float) or not (h > 0.00)):
                raise ValueError(f"h invalid. idx: {idx}, field: v. content: {h}")
            
            l = raw.get("l")
            if (not isinstance(l, float) or not (l > 1.0)):
                raise ValueError(f"l invalid. idx: {idx}, field: l. content: {l}")
            
            c = raw.get("c")
            if ((not isinstance(c, float)) or not (h > 0.00)):
                raise ValueError(f"c invalid. idx: {idx}, field: c. content: {c}")

            v = raw.get("v")
            if ((not isinstance(v, float)) or not (v > 0.00)):
                raise ValueError(f"v invalid. idx: {idx}, field: v. content: {v}")
            
            a = raw.get("a")
            if ((not isinstance(a, float)) or not (a > 0.00)):
                raise ValueError(f"a invalid. idx: {idx}, field: a. content: {a}")

            pc = raw.get("pc")
            if ((not isinstance(pc, float)) or not (pc > 0.00)):
                raise ValueError(f"pc invalid. idx: {idx}, field: pc. content: {pc}")

            sf = raw.get("sf")
            if ((not isinstance(sf, int)) or not (sf == 0 or sf == 1)):
                raise ValueError(f"sf invalid. idx: {idx}, field: sf. content: {sf}")

            result.append(StockExchangeDailyEntity(t=t, o=o, h=h, l=l, c=c, v=v, a=a, pc=pc, sf=sf))
        
        return result