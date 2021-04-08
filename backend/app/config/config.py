from typing import Dict, Optional
from pydantic import BaseModel, BaseSettings


class MfaParamsModel(BaseModel):
    mfa_url: Optional[str] = "12"
    oauth_type: Optional[int] = 12
    share_secret: Optional[str] = '12'
    app_name: Optional[str] = '12'
    static_password: Optional[str] = '12'
    api_gateway_id: Optional[str]


class Settings(BaseSettings):
    """
    配置参数
        env: 运行环境
        editor_auth: 编辑页面的权限
        api_prefix: 接口路径前缀
        sqlalchemy_database_url: 数据库url
        cms_token_url: CMS身份校验url
        cms_token_headers: CMS身份校验Headers
        debug: DEBUG模式
    """
    env: str
    debug: bool
    api_prefix: str = ""
    salt: str
    all_origins: str
    sqlalchemy_database_url: str
    redis_url: str
    redis_token_prefix: str
    redis_login_prefix: str
    login_failed_prefix: str
    token_expire_time_in_seconds: int
    login_expire_time_in_seconds: int
    s3_url: str
    s3_bucket: str
    s3_region: str
    s3_aws_access_key_id: str
    s3_aws_secret_access_key: str
    admin_user_mapping: dict
    mfa_params: dict
    secret_key: str
    access_token_expire_minutes: int
    refresh_token_expire_minutes: int
    application_image_path: str
    image_whitelisting: str
    audit_log_path: Optional[str]
    check_history_password_duplicate: bool
    mail_params: dict

    class Config:
        import os
        env_file = f'{os.path.dirname(os.path.dirname(os.path.abspath(__file__)))}/config/.env'
        env_file_encoding = 'utf-8'
        env_prefix = 'labor_hour'
        fields = {
            'env': {
                'env': 'ENVIRONMENT'
            },
            'debug': {
                'env': 'DEBUG'
            },
            'api_prefix': {
                "env": "API_PREFIX",
            },
            'salt': {
                'env': 'PASSWORD_SALT'
            },
            'all_origins': {
                'env': "ALL_ORIGINS"
            },
            'sqlalchemy_database_url': {
                'env': 'SQLALCHEMY_DATABASE_URL',
            },
            'redis_url': {
                'env': "REDIS_URL"
            },
            'redis_token_prefix': {
                'env': "REDIS_TOKEN_PREFIX"
            },
            'redis_login_prefix': {
                'env': "REDIS_LOGIN_PREFIX"
            },
            'login_failed_prefix': {
                'env': "LOGIN_FAILED_PREFIX"
            },
            'token_expire_time_in_seconds': {
                'env': "TOKEN_EXPIRE_TIME_IN_SECONDS"
            },
            'login_expire_time_in_seconds': {
                'env': "LOGIN_EXPIRE_TIME_IN_SECONDS"
            },
            'mail_params': {
                'env': "MAIL_PARAMS"
            },
            's3_url': {
                'env': 'S3_URL_CN',
            },
            's3_bucket': {
                'env': 'S3_BUCKET_CN',
            },
            's3_region': {
                'env': "S3_REGION_CN"
            },
            's3_aws_access_key_id': {
                'env': 'S3_AWS_ACCESS_KEY_ID',
            },
            's3_aws_secret_access_key': {
                'env': "S3_AWS_SECRET_ACCESS_KEY_CN"
            },
            'admin_user_mapping': {
                'env': "ADMIN_USER_MAPPING"
            },
            'mfa_params': {
                'env': "MFA_PARAMS"
            },
            'secret_key': {
                'env': "SECRET_KEY"
            },
            'access_token_expire_minutes': {
                'env': "ACCESS_TOKEN_EXPIRE_MINUTES"
            },
            'refresh_token_expire_minutes': {
                'env': "REFRESH_TOKEN_EXPIRE_MINUTES"
            },
            'application_image_path': {
                'env': 'APPLICATION_IMAGE_PATH'
            },
            'image_whitelisting': {
                'env': 'IMAGE_WHITELISTING'
            },
            'audit_log_path': {
                'env': 'AUDIT_LOG_PATH'
            },
            'check_history_password_duplicate': {
                'env': 'CHECK_HISTORY_PASSWORD_DUPLICATE'
            },
        }


settings = Settings()
