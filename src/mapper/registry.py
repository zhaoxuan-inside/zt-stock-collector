from typing import Type, Any, List
from .base import Mapper

class MapperRegistry:
    
    _mappers: List[Type[Mapper]] = []

    @classmethod
    def register(cls, mapper_cls: Type[Mapper]) -> None:
        if mapper_cls in cls._mappers:
            return
        
        cls._mappers.append(mapper_cls)

    @classmethod
    def get_mapper(cls, data: Any) -> Type[Mapper] | None:
        for mapper_cls in cls._mappers:
            instanct = mapper_cls()
            if instanct.can_handle(data):
                return mapper_cls;
        return None