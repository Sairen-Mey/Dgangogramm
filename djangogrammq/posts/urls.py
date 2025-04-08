from django.urls import path
from . import views
urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('example/', views.example, name='example'),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('', views.post_list, name='post_list'),
    path('create_post/', views.PostCreateView.as_view(), name='create_post'),
]



# Feed - зробити!!!