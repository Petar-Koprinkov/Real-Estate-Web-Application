from django.contrib.auth import get_user_model
from django.db import models

from real_estate_web_application.real_estate.models import Properties

UserModel = get_user_model()


class CommentModel(models.Model):
    comment = models.TextField()

    date = models.DateTimeField(auto_now_add=True)

    property = models.ForeignKey(
        to=Properties,
        on_delete=models.CASCADE,
        related_name='comments',
    )

    user = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
        related_name='comments'
    )

    class Meta:
        ordering = ['-date']
