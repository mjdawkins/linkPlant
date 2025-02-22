from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Profile, Link

# Create your views here.
class LinkListView(ListView):
    # template called model_list.html -> link_list.html
    model = Link
    
class LinkCreateView(CreateView):
    model = Link
    # here is where the form is created, __all__ means that all the fields within the table will be created in th form
    fields = "__all__"
    # where to send user when they successfully created a link/completed the form
    success_url = reverse_lazy('link-list')
    
    # createview also creates a template model_form which would be link_form.html

class LinkUpdateView(UpdateView):
    model = Link
    fields = ['text', 'url']
    success_url = reverse_lazy('link-list')
    
    # UpdateView uses the same table as createview so it will be link_form.html
    
    
class LinkDeleteView(DeleteView):
    model = Link
    success_url = reverse_lazy('link-list')
    # this class expects a model_confirm_delete.html file so we need to create link_confirm_delete.html
    
    
def profile_view(request, profile_slug):
    profile = get_object_or_404(Profile, slug=profile_slug)
    links = profile.links.all()
    context = {
        'profile': profile,
        'links': links
    }
    return render(request, 'link_tree/profile.html', context)
    