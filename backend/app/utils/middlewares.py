from fastapi import Request, Response
from app.db.orm import SessionLocal


def db_session_middleware(request: Request, call_next):
    """
    数据库连接中间件
    """
    response = Response("Internal server error", status_code=503)
    try:
        request.state.db = SessionLocal()
        response = call_next(request)
    finally:
        request.state.db.close()
    return response


async def process_cookies_record_middleware(request: Request, call_next):
    """
    运行时Cookie中间件
    """
    response = Response("Internal server error", status_code=500)
    response = await call_next(request)
    if hasattr(request.state, "access_token") and request.state.access_token is not None:
        response.headers["Authorization"] = "Bearer %s" % request.state.access_token
    return response
