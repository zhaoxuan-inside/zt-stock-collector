from typing import Final
import os

DOMAIN: Final[str] = "https://api.zhituapi.com"
QUERY_STOCK_BASIC_INFO: Final[str] = "/hs/list/all"
TOKEN: Final[str] = str(os.getenv("TOKEN", "1"))