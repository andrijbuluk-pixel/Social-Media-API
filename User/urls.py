from django.urls import path, include
from rest_framework import routers

from User.views import (
    RegisterUser,
    LoginUser,
    UserDetail,
)

app_name = "User"

router = routers.DefaultRouter()

router.register("register", RegisterUser, basename="UserRegistration")
router.register("login", LoginUser, basename="Login")
router.register("users", UserDetail, basename="UserDetail")

urlpatterns = [
    path("", include(router.urls)),
]