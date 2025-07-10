from authx import AuthXConfig, AuthX

auth_config = AuthXConfig()
auth_config.JWT_SECRET_KEY = "123"
auth_config.JWT_ACCESS_COOKIE_NAME = "access_token"
auth_config.JWT_TOKEN_LOCATION = ['headers']

security = AuthX(config=auth_config)

