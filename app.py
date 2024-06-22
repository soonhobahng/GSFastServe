import os
import uvicorn

from fastapi import FastAPI
from fastapi import status
from fastapi.middleware.cors import CORSMiddleware
from routes import router
from exceptions import server_error_exception, not_found_error_exception, forbidden_error_exception, unauthorized_error_exception


def create_app():
    app = FastAPI()

    app.add_exception_handler(status.HTTP_500_INTERNAL_SERVER_ERROR, server_error_exception)
    app.add_exception_handler(status.HTTP_404_NOT_FOUND, not_found_error_exception)
    app.add_exception_handler(status.HTTP_403_FORBIDDEN, forbidden_error_exception)
    app.add_exception_handler(status.HTTP_401_UNAUTHORIZED, unauthorized_error_exception)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["*"],
    )

    app.include_router(router)

    return app


app_ = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app_", reload=True)
