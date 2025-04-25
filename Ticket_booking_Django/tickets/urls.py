# tickets/urls.py
from django.urls import path
from . import views  # Import views like this
from django.contrib.auth import views as auth_views

app_name = 'tickets'

urlpatterns = [
    # User URLs
    path('', views.ShowListView.as_view(), name='show_list'),
    path('<int:pk>/', views.ShowDetailView.as_view(), name='show_detail'),
    path('<int:pk>/book/', views.BookShowView.as_view(), name='book_show'),
    path('my-bookings/', views.BookingHistoryView.as_view(), name='booking_history'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),

    # Admin URLs
    path('admin/shows/', views.AdminShowListView.as_view(), name='admin_show_list'),
    path('admin/shows/new/', views.AdminShowCreateView.as_view(), name='admin_show_create'),
    path('admin/shows/<int:pk>/edit/', views.AdminShowUpdateView.as_view(), name='admin_show_update'),
    path('admin/shows/<int:pk>/delete/', views.AdminShowDeleteView.as_view(), name='admin_show_delete'),
    path('admin/bookings/', views.AdminBookingListView.as_view(), name='admin_booking_list'),
]