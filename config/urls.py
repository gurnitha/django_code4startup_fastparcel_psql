# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

# Django locals
from apps.core import views  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),

    # users
    path('sign-in/', auth_views.LoginView.as_view(template_name="registration/sign_in.html")),
    path('sign-out/', auth_views.LogoutView.as_view(next_page="/")),

    path('customer/', views.customer_page),
    path('courier/', views.courier_page),
]