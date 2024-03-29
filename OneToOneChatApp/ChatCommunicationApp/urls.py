from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.front_page, name='frontpage'),
    path('signup/', views.signup, name='signup'),
    path("login/", auth_views.LoginView.as_view(template_name= 'ChatCommunicationApp/login.html'), name="logout"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
