from fastapi import FastAPI
from app.config.config import settings
from app.api import router as api_router
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
    # 添加路由
    application.include_router(
        router=api_router,
        prefix=settings.api_prefix
    )
    return application


app = get_application()

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", reload=True, port=8000, debug=True)
