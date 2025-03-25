import json
from typing import Optional

from typing_extensions import TypeVar, Generic

T = TypeVar('T')

class BaseResponse(Generic[T]):
    data : T
    status_code : int
    message : str
    def __init__(self, data, message, status_code):
        self.data = data
        self.message = message
        self.status_code = status_code

    def to_dict(self) -> dict:
        return self.__dict__

    def __str__(self):
        return json.dumps(self.__dict__)