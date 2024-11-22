from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from real_estate_web_application.real_estate.forms import LocationForm, CreatePropertyForm
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
    paginate_by = 3


class AddPropertyView(CreateView):
    model = Properties
    form_class = CreatePropertyForm
    template_name = 'real-estate/add-property.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        real_estate = form.save(commit=False)
        real_estate.owner = self.request.user
        real_estate.save()
        return super().form_valid(form)















