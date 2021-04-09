from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.config import settings
from app.api import router as api_router
from starlette.middleware.base import BaseHTTPMiddleware
from app.utils.middlewares import db_session_middleware
import uvicorn


def get_application() -> FastAPI:
    application = FastAPI(
        title='后台管理系统',
        description="基于fastapi后端服务",
        version="0.1.0",
        openapi_url="%s/openapi.json" % settings.api_prefix,
        swagger_ui_oauth2_redirect_url="%s/docs/oauth2-redirect" % settings.api_prefix,
        docs_url="%s/docs" % settings.api_prefix,
        redoc_url="%s/redoc" % settings.api_prefix,
    )
    # 允许跨域请求
    application.add_middleware(
        middleware_class=CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
        expose_headers=["x-auth-token"],
    )
    # 数据库链接
    application.add_middleware(
        middleware_class=BaseHTTPMiddleware,
        dispatch=db_session_middleware
    )
    # 添加路由
    application.include_router(
        router=api_router,
        prefix=settings.api_prefix
    )
    return application


app = get_application()

if __name__ == '__main__':
    uvicorn.run('main:app', host="127.0.0.1", reload=True, port=8008, debug=True)
