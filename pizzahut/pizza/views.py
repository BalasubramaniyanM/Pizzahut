from django.shortcuts import render
from .forms import PizzaForm
from .models import Pizza
from .forms import PizzaForm, MultiplePizzaForm
from django.forms import formset_factory

# Create your views here.
def homepage(request):
    return render(request,'pizza/home.html')

def order(request):
    multiple_pizza_form = MultiplePizzaForm()
    created_pizza_pk = None
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            note = 'This for ordering %s, %s, %s size pizza'%(filled_form.cleaned_data['topping1'],
                                                              filled_form.cleaned_data['topping2'],
                                                              filled_form.cleaned_data['size'])
            created_pizza = filled_form.save()
            created_pizza_pk = created_pizza.id
            # print(filled_form.cleaned_data['topping1'])
            # print(filled_form['topping1'])
            # form_obj = PizzaForm(topping1=filled_form.cleaned_data['topping1'],
            #                      topping2=filled_form.cleaned_data['topping2'],
            #                      size=filled_form.cleaned_data['size'],)


        else:
            note = 'Sorry please try again'
        new_form = PizzaForm()   #empty form
        return render(request,'pizza/order.html',{'pizzaform':filled_form,'note':note,'multiple_pizza_form':multiple_pizza_form,'created_pizza_pk':created_pizza_pk})
    else:
        form = PizzaForm()
        return render(request, 'pizza/order.html', {'pizzaform': form,'multiple_pizza_form':multiple_pizza_form,})

def pizzas(request):
    no_of_pizzas = 2
    if request.method == 'GET':
        filled_multiple_pizza_form = MultiplePizzaForm(request.GET)
        if filled_multiple_pizza_form.is_valid():
            no_of_pizzas = filled_multiple_pizza_form.cleaned_data['number']
    print(no_of_pizzas)
    pizza_formset = formset_factory(PizzaForm,extra=no_of_pizzas)  #formset
    formset = pizza_formset()    #empty formset
    if request.method == 'POST':
        filled_formset = pizza_formset(request.POST)
        if filled_formset.is_valid():
            for form in filled_formset:
                form.save()
            note = 'Thanks your order was placed successfully!!'
        else:
            note = 'Sorry order not placed, please tryagain...'
        return render(request, 'pizza/pizzas.html',{'note':note})

    return render(request,'pizza/pizzas.html',{'formset':formset})



def edit(request,pk):
    note = ''
    pizza = Pizza.objects.get(pk = pk)     # saved order model objectPizzaForm
    form = PizzaForm(instance=pizza)       # placed order form was collected
    if request.method == 'POST':
        edited_form = PizzaForm(request.POST,instance=pizza)
        if edited_form.is_valid():
            edited_form.save()
            note = 'Order Edited Successfully'
        else:
            note = 'Sorry please tryagain...'

    return render(request,'pizza/edit.html',{'pizzaform':form , 'pk':pk, 'note':note})



