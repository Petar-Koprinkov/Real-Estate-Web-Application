from django.contrib.auth import get_user_model, login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.views import LoginView
from django.db.models import Max, Min, Avg, Count, DecimalField
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, TemplateView
from real_estate_web_application.accounts.forms import CustomUserCreationForm, EditProfileForm
from real_estate_web_application.accounts.models import Profile
from real_estate_web_application.real_estate.models import Properties
from django.db.models import Value as V
from django.db.models.functions import Coalesce

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


class ProfileDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'accounts/profile-details.html'

    def test_func(self):
        if self.request.user.is_superuser:
            return True

        user = get_object_or_404(UserModel, pk=self.kwargs['pk'])
        if self.request.user != user:
            return False

        return True


class ProfileEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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

    def test_func(self):
        if self.request.user.is_superuser:
            return True

        user = get_object_or_404(UserModel, pk=self.kwargs['pk'])
        if self.request.user != user:
            return False

        return True


class ProfileDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Profile
    success_url = reverse_lazy('home')
    template_name = 'accounts/delete-page.html'

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.delete()
        return redirect(self.get_success_url())

    def test_func(self):
        if self.request.user.is_superuser:
            return True

        user = get_object_or_404(UserModel, pk=self.kwargs['pk'])
        if self.request.user == user:
            return True


class StatisticView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'accounts/statistics.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['max_value'] = Properties.objects.aggregate(
            max_value=Coalesce(Max('value', output_field=DecimalField()), V(0, output_field=DecimalField()))
        )['max_value']
        context['min_value'] = Properties.objects.aggregate(
            min_value=Coalesce(Min('value', output_field=DecimalField()), V(0, output_field=DecimalField()))
        )['min_value']
        avg_value = Properties.objects.aggregate(
            avg_value=Coalesce(Avg('value', output_field=DecimalField()), V(0, output_field=DecimalField()))
        )['avg_value']
        context['avg_value'] = round(avg_value, 2)
        exposure_counts = list(
            Properties.objects.values('exposure').annotate(count=Count('exposure')).order_by('-count'))
        context['most_common_exposure'] = exposure_counts[0]['exposure'] if exposure_counts else 'N/A'
        context['least_common_exposure'] = exposure_counts[-1]['exposure'] if exposure_counts else 'N/A'
        type_counts = list(Properties.objects.values('type').annotate(count=Count('type')).order_by('-count'))
        context['most_common_type'] = type_counts[0]['type'] if type_counts else 'N/A'
        context['least_common_type'] = type_counts[-1]['type'] if type_counts else 'N/A'
        return context

    def test_func(self):
        if self.request.user.is_superuser:
            return True

        if self.request.user.user_type != 'Investor':
            return False

        return True
