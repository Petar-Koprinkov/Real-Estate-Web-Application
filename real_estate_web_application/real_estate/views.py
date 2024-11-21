from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from real_estate_web_application.real_estate.forms import LocationForm
from real_estate_web_application.real_estate.models import Location, Properties


class CreateLocationView(CreateView):
    model = Location
    form_class = LocationForm
    template_name = 'real-estate/city.html'
    success_url = reverse_lazy('home')


class PropertyListView(ListView):
    model = Properties
    context_object_name = 'properties'
    template_name = 'real-estate/properties.html'
    paginate_by = 2

