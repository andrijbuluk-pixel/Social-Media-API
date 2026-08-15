from django.db import models

from Social_media_API.settings import AUTH_USER_MODEL


class Post(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.TextField(max_length=500)
    image = models.ImageField(upload_to="media/", blank=True, null=True)
    hashtag = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.post}"


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_like")
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_like")


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comment_post")
    text = models.TextField(max_length=500, blank=True, null=True)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_comment")


class Follow(models.Model):
    follower = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="follower_set")
    following = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="following_set")
