import json
from mapper.registry import MapperRegistry
from db.stock_basic_info_pg_connector import StockBasicInfoConnector
from db.stock_basic_info_entity import StockBasicInfoEntity
from dto.stock import StockBasicInfo
from .http_extractor import HttpExtractor

class StockBasicInfoProcessor:

    def __init__(self, dsn: str, extrator: HttpExtractor):
        self._dsn = dsn
        self._extrator = extrator
    
    def process(self) -> int:

        resp = self._extrator.send_request()

        raw = json.loads(resp)
        mapper_cls = MapperRegistry.get_mapper(raw)
        if not mapper_cls:
            raise
        
        mapper = mapper_cls()
        items: list[StockBasicInfo] = mapper.map(raw)

        if not items:
            return 0

        rows = []
        #  {'dm': '688818.SH', 'mc': '电科蓝天', 'jys': 'SH'}
        for item in items:
            dm = item.dm
            dm_arr = dm.split('.')
            code = dm_arr[0]
            exchanger = dm_arr[1]
            ele = StockBasicInfoEntity(code, item.mc, exchanger)
            rows.append(ele)

        with StockBasicInfoConnector(self._dsn) as connector:
            return connector.insert(rows)