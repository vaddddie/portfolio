from authx import AuthXConfig, AuthX

auth_config = AuthXConfig()
auth_config.JWT_SECRET_KEY = "123"
auth_config.JWT_ACCESS_COOKIE_NAME = "access_token"
JWT_COOKIE_CSRF_PROTECT = False
auth_config.JWT_TOKEN_LOCATION = ['cookies']

security = AuthX(config=auth_config)

