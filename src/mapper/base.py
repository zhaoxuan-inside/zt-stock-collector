from abc import abstractmethod
from typing import Any, List, Generic, TypeVar

T = TypeVar('T')

class Mapper(Generic[T]):

    @abstractmethod
    def can_handle(self, data: Any) -> bool:
        pass

    @abstractmethod
    def map(self, data: Any) -> List[T]:
        pass