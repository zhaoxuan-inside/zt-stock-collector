import re
from typing import Any, List, Dict
from .base import Mapper
from dto.stock_basic_info import StockBasicInfo

class StockBasicInfoMapper(Mapper):

    def check_item(self, data: dict) -> bool:
        return "dm" in data and "mc" in data and "jys" in data

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
    
    def map(self, data: Any) -> List[StockBasicInfo]:
        match data:
            case dict():
                items = [data]
            case list():
                items = data
            case _:
                raise TypeError("invalid data type.")
            
        result = []

        for idx, raw in enumerate(items):
            dm = raw.get("dm")
            if (not isinstance(dm, str) or not (dm := dm.strip())):
                raise ValueError(f"data invalid. idx: {idx}, field: dm. content: {dm}")
            mc = raw.get("mc")
            if (not isinstance(mc, str) or not (mc := mc.strip())):
                raise ValueError(f"data invalid. idx: {idx}, field: mc. content: {mc}")
            jys = raw.get("jys")
            if (not isinstance(jys, str) or not (jys := jys.strip())):
                raise ValueError(f"data invalid. idx: {idx}, field: jys. content: {jys}")
            
            result.append(StockBasicInfo(dm=dm, mc=mc, jys=jys))
        
        return result