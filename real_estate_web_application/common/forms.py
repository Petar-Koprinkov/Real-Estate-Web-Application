from django import forms

from real_estate_web_application.common.models import CommentModel


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = CommentModel
        fields = ('comment',)

        widgets = {
            'comment': forms.Textarea(attrs={'placeholder': 'Add comment...'}),
        }
