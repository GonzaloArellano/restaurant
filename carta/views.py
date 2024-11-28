from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Menu
from .forms import ReviewForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy

# Create your views here.

class MenuListView(ListView):
    model = Menu
    template_name = 'carta/list-view.html'
    context_object_name = 'menus'

@method_decorator(login_required, name='dispatch')
class MenuCreateView(CreateView):
    model = Menu
    template_name = 'carta/create-view.html'
    success_url = reverse_lazy('list')
    form_class = ReviewForm
@method_decorator(login_required, name='dispatch')
class MenuDeleteView(DeleteView):
    model = Menu
    template_name = 'carta/delete-view.html'
    success_url = reverse_lazy('list')

class MenuDetailView(DetailView):
    model = Menu
    template_name = 'carta/detail-view.html'
    context_object_name = 'menu'