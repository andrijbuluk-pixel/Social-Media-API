from django.urls import path
from media_system.views import (
    CreatePostApi,
    DetailPostApiCRUD,
    CreateCommentApi,
    AddLikeApi,
)

app_name = 'media_system'

urlpatterns = [
    path("create/", CreatePostApi.as_view(), name="create_post" ),
    path("detail/<int:pk>/", DetailPostApiCRUD.as_view(), name="detail_post"),
    path("comment/", CreateCommentApi.as_view(), name="create_comment"),
    path("like/<int:pk>/", AddLikeApi.as_view(), name="add_like"),
]