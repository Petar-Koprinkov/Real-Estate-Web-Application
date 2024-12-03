from django.contrib.auth import get_user_model
from django.db import models

from real_estate_web_application.common.validators import BadLanguageValidator
from real_estate_web_application.real_estate.models import Properties

UserModel = get_user_model()


class CommentModel(models.Model):
    comment = models.TextField(
        validators=[BadLanguageValidator(['bad_word', 'very_bad_word'])]
    )

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

    def __str__(self):
        return self.comment

    class Meta:
        ordering = ['-date']
