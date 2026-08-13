from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
    TokenBlacklistView,
)

from User.views import (
    CreateUserView,
    UserDetailView,
    AvatarUploadView,
    UserSearchView,
)

app_name = "User"


urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("register/", CreateUserView.as_view(), name="register"),
    path("logout/", TokenBlacklistView.as_view(), name="logout"),

    path("me/", UserDetailView.as_view(), name="user_detail"),
    path("me/shearch/", UserSearchView.as_view(), name="shearch"),
    path("me/upload-avatar/", AvatarUploadView.as_view(), name="avatar"),
]
