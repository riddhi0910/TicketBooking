# booking_system/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls), 
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('', RedirectView.as_view(url='shows/'), name='home'),
    path('accounts/', include('accounts.urls')),
    path('shows/', include('tickets.urls',namespace='tickets')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html')),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='your_app/login.html')),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]
