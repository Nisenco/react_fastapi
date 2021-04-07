from fastapi import APIRouter

from app.api.v1.auth import login

router = APIRouter()

router.include_router(login.router, tags=['user'], prefix='users')
