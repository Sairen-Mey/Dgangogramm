from django.shortcuts import render, redirect, get_object_or_404
from django.template import loader, Template
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm, PostForm
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import User, Post, Image
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


def registration(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account create')
            return redirect('home')
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


@login_required
def home(request):
    user = get_object_or_404(User, email=request.user.email)
    return render(request, 'home.html', {'user': user})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.user
            login(request, user)
            messages.success(request, 'login is cool')
            return redirect('home')
        else:
            messages.error(request, 'date is wrong')
    else:
        form = LoginForm()
    return render(request,'login.html', {'form': form})


def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'post_list.html', {'posts': posts})


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'create_post.html'
    success_url = reverse_lazy('create_post')

    def form_valid(self, form):
        response = super().form_valid(form)
        files = form.cleaned_data.get('images')
        if files:
            for f in files:
                Image.objects.create(post=self.object, image=f)
        return response
