from django.urls import path
from media_system.views import (
    CreatePostApi,
    DetailPostApiCRUD,
    CreateCommentApi,
    AddLikeApi,
    PostSearchApi,
)

app_name = 'media_system'

urlpatterns = [
    path("create/", CreatePostApi.as_view(), name="create_post"),
    path("detail/<int:pk>/", DetailPostApiCRUD.as_view(), name="detail_post"),
    path("comment/", CreateCommentApi.as_view(), name="create_comment"),
    path("like/<int:pk>/", AddLikeApi.as_view(), name="add_like"),
    path("search/", PostSearchApi.as_view(), name="search_post"),
]
