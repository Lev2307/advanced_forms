from django.shortcuts import render, redirect
from pizzas.models import PizzaModel
from .models import OrderModel
from .forms import CreateForm, CreateOrderModelForm
from django.forms import modelformset_factory
# Create your views here.

def index(request):
    return render(request, 'index.html')
def create_order(request):
    order_form = CreateForm(request.POST or None)
    context = {
        'pizzas': PizzaModel.objects.all(),
        'order_form': order_form
    }
    if order_form.is_valid():
        address = order_form.cleaned_data.get('address')
        order = dict(order_form.data).get('choice')
        pizza_objects = [PizzaModel.objects.get(id=i) for i in order]
        new_order = OrderModel.objects.create(address=address)
        new_order.pizza_order.add(*pizza_objects)
        new_order.save()
        return redirect('createorder')
    return render(request, 'order/create_order.html', context=context)

def create_model_order(request, *args, **kwargs):
    model_form = CreateOrderModelForm(request.POST or None)
    OrderFormSet = modelformset_factory(OrderModel, form=CreateOrderModelForm, extra=2)
    model_form = OrderFormSet(
        request.POST or None,
        queryset=OrderModel.objects.none(),
        initial=[{'address': 'modelformset street'}]
        )
    # print(model_form.data)
    # if model_form.is_valid():
    #     model_form.save()
    #     return redirect('createmodelorder')
    context = {
        'pizzas': PizzaModel.objects.all(),
        'form': model_form
    }
    return render(request, 'order/create_model_order.html', context=context)