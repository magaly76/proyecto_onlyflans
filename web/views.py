from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Flan, ContactForm
from .forms import ContactFormForm 
from django.contrib.auth.decorators import login_required

    # Create your views here.
def index(request):
    public_flans = Flan.objects.filter(is_private=False)
    #all_flans = Flan.objects.all()
    return render(request, 'index.html', {'public_flans': public_flans})

@login_required
def welcome(request):
    private_flans = Flan.objects.filter(is_private=True)
    return render(request,'welcome.html',{'private_flans': private_flans})

def about(request):
    return render(request, 'about.html', {})

def contact(request):
    if request.method == 'POST':
        form = ContactFormForm(request.POST)
     
        if form.is_valid():
            contact_form=ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito/')
        else:  
            print("Formulario no válido. Errores:", form.errors)
    else:
        form = ContactFormForm()
            
    return render(request, 'contact.html', {'form': form})

def exito(request):
    return render(request, 'exito.html', {})

def login(request):
    return render(request, 'login.html', {})

def logged_out(request):
    return render(request, 'logged_out.html', {})

def carousel(request):
    public_flans = Flan.objects.filter(is_private=False)
    #all_flans = Flan.objects.all()
    return render(request, 'carousel.html', {'public_flans': public_flans})

@login_required
def recipe(request):
    categories = ['tradicional', 'innovador', 'sin_azucar']
    selected_category = request.GET.get('category', '')
    flans = Flan.objects.filter(category=selected_category) if selected_category else Flan.objects.all()
    return render(request, 'recipe.html', {'flans': flans, 'categories': categories, 'selected_category': selected_category})

def recipe_detail(request, slug):
    flan = get_object_or_404(Flan, slug=slug)
    return render(request, 'recipe_detail.html', {'flan': flan})