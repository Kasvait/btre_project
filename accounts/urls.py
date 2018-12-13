from django.urls import path

from . import views

urlpatterns = [
    # we will need 4 different Urls, which does not come automatically so we need to create urls page
    # path login (first input )
    # views.login is a method name or a funcion name;
    # name is login'
    # then you have to input these methods inside the view. Until its not, you will get errors.
    # you also need to input to the main app urls.py (btre)

    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard')
]