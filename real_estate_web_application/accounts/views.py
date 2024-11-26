from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.db.models import Max, Min, Avg, Count
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, TemplateView
from real_estate_web_application.accounts.forms import CustomUserCreationForm, EditProfileForm
from real_estate_web_application.accounts.models import Profile
from real_estate_web_application.real_estate.models import Properties

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


class ProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'accounts/profile-details.html'


class ProfileEditView(LoginRequiredMixin, UpdateView):
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


class ProfileDeleteView(LoginRequiredMixin, DeleteView):
    model = Profile
    success_url = reverse_lazy('home')
    template_name = 'accounts/delete-page.html'

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return redirect(self.get_success_url())


class StatisticView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/statistics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['max_value'] = Properties.objects.aggregate(max_value=Max('value'))['max_value']
        context['min_value'] = Properties.objects.aggregate(min_value=Min('value'))['min_value']
        avg_value = Properties.objects.aggregate(min_value=Avg('value'))['min_value']
        context['avg_value'] = round(avg_value, 2)
        exposure_counts = Properties.objects.values('exposure').annotate(count=Count('exposure')).order_by('-count')
        context['most_common_exposure'] = exposure_counts.first()['exposure']
        context['least_common_exposure'] = exposure_counts.last()['exposure']
        exposure_counts = Properties.objects.values('type').annotate(count=Count('type')).order_by('-count')
        context['most_common_type'] = exposure_counts.first()['type']
        context['least_common_type'] = exposure_counts.last()['type']
        return context
