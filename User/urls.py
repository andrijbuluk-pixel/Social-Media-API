from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from User.views import (
    CreateUserView,
    UserDetailView,
    AvatarUploadView,
)

app_name = "User"


urlpatterns = [
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("register/", CreateUserView.as_view(), name="register"),

    path("me/", UserDetailView.as_view(), name="user_detail"),
    path("me/upload-avatar/", AvatarUploadView.as_view(), name="avatar"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
