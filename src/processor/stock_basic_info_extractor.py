from requests import Response
from .http_extractor import HttpExtractor
from src.consts.zhitu_consts import DOMAIN, PARAM_STOCK_BASIC_INFO, QUERY_TOKEN

class StockBasicInfoExtractor(HttpExtractor):

    def __init__(self):
        super().__init__(DOMAIN, QUERY_TOKEN)

    def send_request(self) -> str:
        resp = super().request(PARAM_STOCK_BASIC_INFO)
        return resp.json()