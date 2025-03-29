import json
from typing import Optional

from typing_extensions import TypeVar, Generic

from utils.constant import ConstantUtil

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

    @staticmethod
    def success(data: T, message: Optional[str] = None):
        if message is not None:
            return BaseResponse(data, message, ConstantUtil.HttpStatus.SUCCESS_CODE).to_dict()
        return BaseResponse(data, ConstantUtil.HttpStatus.SUCCESS_MESSAGE, ConstantUtil.HttpStatus.SUCCESS_CODE).to_dict()

    @staticmethod
    def bad_request(data: T = None, message: Optional[str] = None):
        if message is not None:
            return BaseResponse(data, message, ConstantUtil.HttpStatus.BAD_REQUEST_CODE).to_dict()
        return BaseResponse(data, ConstantUtil.HttpStatus.BAD_REQUEST_MESSAGE, ConstantUtil.HttpStatus.BAD_REQUEST_CODE).to_dict()

    @staticmethod
    def internal_server_error(data: T = None, message: Optional[str] = None):
        if message is not None:
            return BaseResponse(data, message, ConstantUtil.HttpStatus.INTERNAL_SERVER_ERROR_CODE).to_dict()
        return BaseResponse(data, ConstantUtil.HttpStatus.INTERNAL_SERVER_ERROR_MESSAGE, ConstantUtil.HttpStatus.INTERNAL_SERVER_ERROR_CODE).to_dict()


    def not_found(data: T = None, message: Optional[str] = None):
        if message is not None:
            return BaseResponse(data, message, ConstantUtil.HttpStatus.NOT_FOUND_CODE).to_dict()
        return BaseResponse(data, ConstantUtil.HttpStatus.NOT_FOUND_MESSAGE, ConstantUtil.HttpStatus.NOT_FOUND_CODE).to_dict()