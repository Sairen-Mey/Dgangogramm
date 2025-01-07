from django.urls import path
from . import views

urlpatterns = [
    path('accounts/registration/', views.registration, name='registration'),
    path('example/', views.example, name='example'),
    path('login/', views.login_view, name='login')
    # path('home', views, name = 'home')
]