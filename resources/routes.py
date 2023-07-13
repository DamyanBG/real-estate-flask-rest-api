from resources.auth_resource import (
    RegisterUser,
    LoginUser,
    RegisterSeller,
    LoginSeller,
    LoginAdmin,
)

routes = (
    (RegisterUser, "/user/register-user"),
    (LoginUser, "/user/login-user"),
    (RegisterSeller, "/user/register-seller"),
    (LoginSeller, "/user/login-seller"),
    (LoginAdmin, "/user/login-admin"),
)