from django import forms
from .models import Pizza


# class PizzaForm(forms.Form):
#     topping1 = forms.CharField(label='Topping1', max_length=100)
#     topping2 = forms.CharField(label='Topping2', max_length=100)
#     size = forms.ChoiceField(label='size', choices=[('small', 'small'),
#                                                     ('medium', 'medium'),
#                                                     ('large', 'large')])

class PizzaForm(forms.ModelForm):   # django model from class
    class Meta:
        model = Pizza
        fields = ['topping1', 'topping2', 'size']


class MultiplePizzaForm(forms.Form):
    # Allows multiple pizzas to be created
    number = forms.IntegerField(min_value=1, max_value=20)