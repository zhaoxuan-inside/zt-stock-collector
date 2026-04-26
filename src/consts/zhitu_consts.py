from typing import Final
import os

DOMAIN: Final[str] = "https://api.zhituapi.com"
PARAM_STOCK_BASIC_INFO: Final[str] = "/hs/list/all"
TOKEN: Final[str] = str(os.getenv("TOKEN", "89912D72-30F7-4A63-BFBA-DE39CDE31575"))
QUERY_TOKEN: Final[str] = "token=" + TOKEN