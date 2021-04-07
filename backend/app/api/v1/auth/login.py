from fastapi import APIRouter, Request, Response, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.database import get_db_session

router = APIRouter()
router.post(
    "/openapi_login",
    summary='OpenAPI后台登录'
)


def openapi_login(
        request: Request,
        response: Response,
        login_info: OAuth2PasswordRequestForm = Depends(),
        db_session: Session = Depends(get_db_session)
):
    pass


router.post(
    "/login",
    summary='OpenAPI后台登录'
)


def login(
    request: Request,
    response: Response,
):
    pass
