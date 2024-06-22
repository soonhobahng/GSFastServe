import os
import json

from pydantic import BaseModel
from fastapi import HTTPException
from fastapi.requests import Request
from fastapi import status
from starlette.responses import JSONResponse

from settings import BASE_DIR


def read_json_file(error_no):
    """
    JSON 파일을 읽고 그 안의 필드 값을 읽어오는 함수입니다.

    Args:
        file_path (str): JSON 파일의 경로

    Returns:
        dict: JSON 파일에 저장된 데이터
    """

    err_file = os.path.join(BASE_DIR + "/templates/errors", error_no)
    try:
        with open(err_file, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print(f"Error: JSON 파일을 찾을 수 없습니다: {err_file}")
        return None
    except json.JSONDecodeError:
        print(f"Error: JSON 파일 파싱에 실패했습니다: {err_file}")
        return None


async def server_error_exception(request: Request, exc: HTTPException):
    data = read_json_file("500")
    return JSONResponse(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, content=data)


async def not_found_error_exception(request: Request, exc: HTTPException):
    data = read_json_file("404")
    return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content=data)


async def forbidden_error_exception(request: Request, exc: HTTPException):
    data = read_json_file("403")
    return JSONResponse(status_code=status.HTTP_403_FORBIDDEN, content=data)


async def unauthorized_error_exception(request: Request, exc: HTTPException):
    data = read_json_file("401")
    return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content=data)
