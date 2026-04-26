from abc import ABC, abstractmethod
import requests
from requests import Response 

class HttpExtractor(ABC):

    def __init__(self, domain: str, query_token: str, timeout: int=3):
        self._domain = domain
        self._query_token = query_token
        self._timeout = timeout

    def request(self, param: str, query: str="") -> Response :
        url: str = self._build_url(param, query)
        return requests.get(url, timeout=self._timeout)
    
    def _build_url(self, param: str, query: str) -> str :
        url: str = self._domain
        if not param:
            url += param
        
        url += "?"
        if not query:
            url += query
        
        url += self._query_token

        return url
    
    @abstractmethod
    def send_request(self) -> str:
        pass