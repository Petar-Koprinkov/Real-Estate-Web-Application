from django.views.generic import ListView

from real_estate_web_application.real_estate.models import Properties


class HomePageView(ListView):
    model = Properties
    template_name = 'common/home.html'
    context_object_name = 'properties'

    def get_queryset(self):
        return Properties.objects.order_by('-value')[:3]





