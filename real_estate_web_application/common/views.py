from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView
from real_estate_web_application.common.forms import CreateCommentForm
from real_estate_web_application.real_estate.models import Properties


class HomePageView(ListView):
    model = Properties
    template_name = 'common/home.html'
    context_object_name = 'properties'

    def get_queryset(self):
        return Properties.objects.order_by('-value')[:3]


@login_required
def create_comment_view(request, pk):
    real_estate = Properties.objects.get(id=pk)
    form = CreateCommentForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            comment = form.save(commit=False)
            comment.property = real_estate
            comment.user = request.user
            comment.save()

        return redirect(request.META['HTTP_REFERER'])
