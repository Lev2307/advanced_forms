from django.shortcuts import render
from .models import PizzaModel

# Create your views here.

def pizza_detail_view(request, *args, **kwargs):
    print(kwargs)
    pizza_obj = PizzaModel.objects.get(name_slug=kwargs.get('slug'))
    context = {'pizza_object': pizza_obj}
    return render(request, 'pizza/pizza_detail.html', context)