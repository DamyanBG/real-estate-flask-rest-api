from resources.auth_resource import (
    RegisterUser,
    LoginUser,
    RegisterSeller,
    LoginSeller,
    LoginAdmin,
    Login,
)
from resources.home_resource import HomeResource, GetHomeResource, HomesResource, HomeDetailsResource

routes = (
    (RegisterUser, "/user/register-user"),
    (LoginUser, "/user/login-user"),
    (RegisterSeller, "/user/register-seller"),
    (LoginSeller, "/user/login-seller"),
    (Login, "/user/login"),
    (LoginAdmin, "/user/login-admin"),
    (HomeResource, "/home"),
    (HomesResource, "/homes"),
    (GetHomeResource, "/home/<int:home_id>"),
    (HomeDetailsResource, "/home-details/<int:home_id>"),
)