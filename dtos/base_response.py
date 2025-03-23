from typing import Optional

from typing_extensions import TypeVar, Generic

T = TypeVar('T')

class BaseResponse(Generic[T]):
    data : Optional[T]
    status_code : int
    message : str
    def __init__(self, data, message, status_code):
        self.data = data
        self.message = message
        self.status_code = status_code

    def to_dict(self):
        return {
            "data" : self.data,
            "message" : self.message,
            "status_code": self.status_code
        }