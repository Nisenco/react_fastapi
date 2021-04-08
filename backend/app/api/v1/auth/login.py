import uuid
import hashlib
from fastapi import APIRouter, Request, Response, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.orm import get_db_session
from app.schemas.schemas_login import LoginModel
from app.db.curd.user import get_user_by_account
from app.utils.security import make_password

router = APIRouter()


@router.post(
    "/openapi_login",
    summary='OpenAPI后台登录'
)
# 显示swager
def openapi_login(
        request: Request,
        response: Response,
        login_info: OAuth2PasswordRequestForm = Depends(),
        db_session: Session = Depends(get_db_session)
):
    pass


@router.post(
    "/login",
    summary='OpenAPI后台登录'
)
def login(
        request: Request,
        response: Response,
        login_info: LoginModel,
        db_session: Session = Depends(get_db_session)
):
    def make_old_password(old_password):
        import hashlib
        PASSWORD_SALT = "asdfaskfdhjasfkjas"
        SECRET_KEY = PASSWORD_SALT
        password = SECRET_KEY + old_password
        # 2.开始加密
        sha1_obj = hashlib.sha1()
        sha1_obj.update(password.encode())
        ret = sha1_obj.hexdigest()
        return ret

    # 获取用户ip地址
    client_ip = request.client.host
    # 获取用户信息
    user = get_user_by_account(db_session, login_info.username)
    if user is None:
        valid = False
    else:
        valid = False
    login_session_id = uuid.uuid4().hex
    m = hashlib.md5()
    m.update(login_session_id.encode("utf-8"))
    login_session_id = m.hexdigest()
    response.set_cookie('login_session_id', login_session_id, expires=60 * 5, samesite="none", secure=True)
    return {"message": "ok"}


@router.post(
    "/password",
    summary='后台管理系统-密码更新'
)
def update_password(
        request: Request,
        response: Response,
        login_info: LoginModel,
        db_session: Session = Depends(get_db_session)
):
    pass
