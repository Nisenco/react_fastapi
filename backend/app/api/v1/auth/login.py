import uuid
import hashlib
import time
from datetime import timedelta, datetime
from fastapi import APIRouter, Request, Response, Depends
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.db.orm import get_db_session
from app.schemas.schemas_login import LoginModel
from app.db.curd.user import get_user_by_account, change_password_by_account
from app.utils.security import make_password
from app.utils.common import make_response
from app.config.config import settings
from app.utils.authorization import create_access_token

router = APIRouter()


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
    # 获取用户ip地址
    client_ip = request.client.host
    # 获取用户信息
    user = get_user_by_account(db_session, login_info.username)
    if user is None:
        return make_response(status=403, message='用户不存在')
    else:
        if make_password(login_info.password) != user.hashed_password:
            return make_response(status=403, message='账户/密码不正确')
    login_session_id = uuid.uuid4().hex
    m = hashlib.md5()
    m.update(login_session_id.encode("utf-8"))
    login_session_id = m.hexdigest()
    response.set_cookie('login_session_id', login_session_id, expires=60 * 5, samesite="none", secure=True)
    # 生成token
    access_token_expires = timedelta(minutes=settings.refresh_token_expire_minutes)
    token_expires_delta = timedelta(minutes=settings.access_token_expire_minutes)
    user_info = {
        "id": user.id,
        "name": user.name,
        "account": user.account,
        # "group_id": user.group_id,
        "is_manager": user.is_manager,
        "role": user.role,
        "token_expire_delta": int(time.mktime((datetime.utcnow() + token_expires_delta).timetuple()))

    }
    access_token = create_access_token(
        data=user_info, expires_delta=access_token_expires
    )
    result = {"access_token": access_token, "token_type": "line"}
    return make_response(data=result)


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
    user = get_user_by_account(db_session, login_info.username)
    if user is None:
        return make_response(status=500, message='没有此账户')
    if login_info.password is None:
        return make_response(status=500, message='密码不能为空')
    user_info = change_password_by_account(db_session, login_info.password, user)
    return make_response(status=200, message='密码更新成功')
