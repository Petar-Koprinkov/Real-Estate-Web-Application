from django.contrib.auth import get_user_model, login
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from real_estate_web_application.accounts.forms import CustomUserCreationForm, EditProfileForm
from real_estate_web_application.accounts.models import Profile

UserModel = get_user_model()


class RegisterView(CreateView):
    model = UserModel
    form_class = CustomUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, self.object)
        return response


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'


class ProfileDetailView(DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'accounts/profile-details.html'


class ProfileEditView(UpdateView):
    model = Profile
    form_class = EditProfileForm
    context_object_name = 'profile'
    template_name = 'accounts/profile-edit.html'

    def get_success_url(self):
        return reverse_lazy(
            'profile-detail',
            kwargs={
                'pk': self.object.pk
            }
        )


class ProfileDeleteView(DeleteView):
    model = Profile
    success_url = reverse_lazy('home')
    template_name = 'accounts/delete-page.html'

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return redirect(self.get_success_url())
