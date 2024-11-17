from django.contrib.auth import get_user_model, login
from django.urls import reverse_lazy
from django.views.generic import CreateView
from real_estate_web_application.accounts.forms import CustomUserCreationForm

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
