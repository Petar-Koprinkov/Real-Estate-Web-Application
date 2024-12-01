from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from real_estate_web_application.accounts.choices import UserTypeChoice
from real_estate_web_application.accounts.models import Profile
from real_estate_web_application.accounts.form_mixins import DisabledMixin

UserModel = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UserModel
        fields = ('username', 'user_type')


class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = '__all__'


class EditProfileForm(forms.ModelForm):
    user_type = forms.ChoiceField(
        choices=UserTypeChoice.choices,
        required=True,
        label="User Type",
    )

    class Meta:
        model = Profile
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.user:
            self.fields['user_type'].initial = self.instance.user.user_type

    def save(self, commit=True):
        profile = super().save(commit=False)
        if commit:
            profile.save()

        if 'user_type' in self.cleaned_data:
            user = profile.user
            user.user_type = self.cleaned_data['user_type']
            if commit:
                user.save()

        return profile


