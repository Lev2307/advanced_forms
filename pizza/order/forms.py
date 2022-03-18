from django import forms
from pizzas.models import PizzaModel
from .models import OrderModel
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Submit, Layout, Field, ButtonHolder

PIZZAS = [(f'{p.id}', f'{p.name}') for p in PizzaModel.objects.all()]
DEL_STATUS = [('Pen', 'Pending'), ('DEL', 'Delivered')]

class CreateForm(forms.Form):

    def __init__(self, *args, **kwargs):
        pass
    address = forms.CharField(required=True)
    choice = forms.ChoiceField(
        choices=PIZZAS,
        help_text='If you wanna some extra. Send us <a href="#">message</a>',
        widget=forms.CheckboxSelectMultiple(attrs={'class': 'pizzas'})
    )
    delivery_status = forms.ChoiceField(
        choices=DEL_STATUS
    )

class CreateOrderModelForm(forms.ModelForm):
    error_css_class = "error-field-class"
    required_css_class = "required-field-class"
    class Meta:
        model = OrderModel
        fields = ['address', 'pizza_order']
        widgets = {
            'address': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your address: '
            }),
            'pizza_order': forms.CheckboxSelectMultiple()
        }