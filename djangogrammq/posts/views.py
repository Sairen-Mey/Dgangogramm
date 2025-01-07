from django.shortcuts import render, redirect
from django.template import loader, Template
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account create')
            return redirect('example')
        else:
            messages.error(request, 'Edit your request on the form')
    else:
        form = RegisterForm()
    return render(request, 'registration.html', {'form': form})

def example(request):
    template: Template = loader.get_template('example.html')
    context = {
        'title': 'Example page',
        'members': ['Alise','Jon', 'Max']
        }
    return HttpResponse(template.render(context))


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.user
            login(request, user)
            messages.success(request, 'login is cool')
            return redirect('example')
        else:
            messages.error(request, 'date is wrong')
    else:
        form = LoginForm()
    return render(request,'login.html', {'form': form})


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
