from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_custom, name='login'),
    path('register/', views.register_custom, name='register'), 
    path('logout/', views.logout_view, name='logout'), 
]