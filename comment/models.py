from django.contrib.auth.models import User
from django.db import models
from core.models import Common
from post.models import Post


class Common_Comment(Common):
    content = models.CharField(max_length=256)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True
        ordering = ["-created_at"]


class Comment(Common_Comment):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class CComment(Common_Comment):
    parent = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="ccomment"
    )

    def __str__(self):
        return self.content


class UserTag(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    who = models.ForeignKey(User, on_delete=models.CASCADE)