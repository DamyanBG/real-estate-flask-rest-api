from resources.auth_resource import (
    RegisterUser,
    LoginUser,
    RegisterSeller,
    LoginSeller,
    LoginAdmin,
    Login,
)
from resources.home_resource import HomeResource, GetHomeResource

routes = (
    (RegisterUser, "/user/register-user"),
    (LoginUser, "/user/login-user"),
    (RegisterSeller, "/user/register-seller"),
    (LoginSeller, "/user/login-seller"),
    (Login, "/user/login"),
    (LoginAdmin, "/user/login-admin"),
    (HomeResource, "/home"),
    (GetHomeResource, "/home/<int:home_id>"),
)