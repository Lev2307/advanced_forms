from django import forms
from pizzas.models import PizzaModel
from .models import OrderModel

PIZZAS = [(f'{p.id}', f'{p.name}') for p in PizzaModel.objects.all()]

class CreateForm(forms.Form):
    address = forms.CharField()
    choice = forms.ChoiceField(choices=PIZZAS, widget=forms.Select(attrs={'class': 'pizza'}))

class CreateOrderModelForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = ['address', 'pizza_order']
        widgets = {
            'pizza_order': forms.CheckboxSelectMultiple()
        }