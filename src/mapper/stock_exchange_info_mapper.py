from typing import Any, List
from .base import Mapper
from dto.stock_exchange_info import StockExchangeInfo

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
    
    def map(self, data: Any) -> List[StockExchangeInfo]:
        match data:
            case dict():
                items = [data]
            case list():
                items = data
            case _:
                raise TypeError("invalid data type.")
            
        result = []

        for idx, raw in enumerate(items):
            date = raw.get("d")
            if (not isinstance(date, str) or not (date := date.strip())):
                raise ValueError(f"data invalid. idx: {idx}, field: d. content: {date}")
            time: str | None = raw.get("t")
            if (not isinstance(time, str) or not (time := time.strip())):
                raise ValueError(f"data invalid. idx: {idx}, field: t. content: {time}")
            value = raw.get("v")
            if (not isinstance(value, int) or not (value > 100)):
                raise ValueError(f"data invalid. idx: {idx}, field: v. content: {value}")
            price = raw.get("p")
            if (not isinstance(price, float) or not (price > 1.0)):
                raise ValueError(f"data invalid. idx: {idx}, field: v. content: {price}")
            order = raw.get("ts")
            if ((not isinstance(order, int)) or (order != 0 and order != 1 and order != 2)):
                raise ValueError(f"data invalid. idx: {idx}, field: v. content: {price}")

            result.append(StockExchangeInfo(d=date, t=time, v=value, p=price, ts=order))
        
        return result
