from media_system.models import Post

from celery import shared_task


@shared_task
def postponed_post_task(post_id):
    try:
        post = Post.objects.get(pk=post_id)
        post.is_published = True
        post.save(update_fields=['is_published'])
        return f"Post {post_id} has been published"
    except Post.DoesNotExist:
        return f"Post {post_id} does not exist"
