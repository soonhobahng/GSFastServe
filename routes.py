import os

from fastapi import FastAPI, Request, Response
from fastapi import Depends, APIRouter, UploadFile, File

router = APIRouter()


@router.get("/")
async def home():
    return {"message": f"GSInsight FastServe!!!"}


@router.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
