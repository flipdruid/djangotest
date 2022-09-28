from .models import Core
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView
from django.urls import reverse_lazy


class IndexView(ListView):
    model               =   Core
    template_name       =   'core/index.html'
    paginate_by         =   10
    context_object_name =   'post_list'

class PollsView(DetailView):
    model               =   Core
    template_name       =   'core/polls.html'
    pk_url_kwarg        =   'pk'
    context_object_name =   'poll'



class AddView(CreateView):
    model               =   Core
    template_name       =   'core/add.html'
    fields              =   '__all__'
    success_url         =   reverse_lazy('core:index')

class EditView(UpdateView):
    model               =   Core
    template_name       =   'core/edit.html'
    fields              =   '__all__'
    pk_url_kwarg        =   'pk'
    success_url         =   reverse_lazy('core:index')

class Delete(DeleteView):
    model               =   Core    
    # fields              =   '__all__'
    pk_url_kwarg        =   'pk'
    success_url         =   reverse_lazy('core:index')
    template_name       =   'core/confirm-delete.html'