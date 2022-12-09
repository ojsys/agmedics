from django.urls import path, include
from . import views


urlpatterns = [
    
    path('login', views.LoginPageView.as_view(), name='login'),
    path('signup', views.signup, name='signup'),
    path('logout/', views.logout_user, name='logout'),
]