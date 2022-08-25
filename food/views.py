from msilib.schema import ListView
from multiprocessing.util import is_abstract_socket_namespace
from re import template
from django.shortcuts import render
from .models import Item
from .forms import ItemForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView,DeleteView,ListView,DetailView,CreateView

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
def index(request):
    item_list=Item.objects.all()
    context = {
        'item_list':item_list
    }
    return render(request,'food/index.html',context=context)

class HomePage(ListView):
    model = Item
    template_name = 'food/index.html'
    context_object_name = 'item_list'



def item(request):
    return render(request,'food/item.html')


def detail(request,pk):
    item = Item.objects.get(pk=pk)
    context = {'item':item}
    return render(request,'food/detail.html',context=context)

class ItemDetailView(DetailView):
    model = Item
    template_name = 'food/detail.html'
    


def create_item(request):
        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ItemForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.cleaned_data.save()
            return HttpResponseRedirect(reverse('food:index'))

    else:
        form = ItemForm()

    return render(request, 'food/item_form.html', {'form': form})

class ItemCreateView(CreateView):
    model = Item
    fields = ['item_name','item_desc','item_price','img']
    template_name = 'food/item_form.html'
    def form_valid(self,form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)
    
    


class ItemUpdateView(LoginRequiredMixin,UpdateView):
    model = Item
    form_class = ItemForm
    
    
    success_url = '/'

class ItemDeleteView(DeleteView):
    model = Item
    success_url = reverse_lazy('food:index')

@login_required
def my_view(request):
    return render(request,'food/my_view.html')



