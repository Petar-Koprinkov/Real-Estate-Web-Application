from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from real_estate_web_application.common.forms import CreateCommentForm
from real_estate_web_application.real_estate.forms import LocationForm, CreatePropertyForm, EditPropertyForm, \
    ParkingForm
from real_estate_web_application.real_estate.models import Location, Properties, Parking


class CreateLocationView(CreateView):
    model = Location
    form_class = LocationForm
    template_name = 'real-estate/city.html'
    success_url = reverse_lazy('home')


class CreateParkingView(CreateView):
    model = Parking
    form_class = ParkingForm
    template_name = 'real-estate/parking.html'
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


class DetailPropertyView(DetailView, CreateView):
    model = Properties
    context_object_name = 'property'
    template_name = 'real-estate/detail-property.html'
    form_class = CreateCommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = self.object.comments.all()
        context['favourite_property'] = self.request.session.get('favourite_property')
        return context


class EditPropertyView(UpdateView):
    model = Properties
    form_class = EditPropertyForm
    template_name = 'real-estate/edit-property.html'
    success_url = reverse_lazy('home')


class DeletePropertyView(DeleteView):
    model = Properties
    success_url = reverse_lazy('home')
    template_name = 'accounts/delete-property.html'
    context_object_name = 'property'

    def delete(self, request, *args, **kwargs):
        real_estate = self.get_object()
        real_estate.delete()
        return redirect(self.get_success_url())


class FavouritePropertyView(View):
    def get(self, request):
        favourite_property = request.session.get('favourite_property')
        context = {}

        if not favourite_property:
            context['favourite_property'] = []
            context['is_favourite'] = False
        else:
            real_estate = Properties.objects.filter(id__in=favourite_property)
            context['is_favourite'] = True
            context['favourite_property'] = real_estate

        return render(request, 'real-estate/favourite-property.html', context)

    def post(self, request):
        favourite_property = request.session.get('favourite_property', [])

        property_id = int(request.POST.get('property_id'))

        if property_id not in favourite_property:
            favourite_property.append(property_id)
        else:
            favourite_property.remove(property_id)
        request.session['favourite_property'] = favourite_property

        return redirect(request.META['HTTP_REFERER'])














