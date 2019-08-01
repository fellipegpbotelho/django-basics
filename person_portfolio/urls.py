from django.urls import path
from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('', views.sign_up, name='user_sign'),
    path('dashboard', views.user_dashboard, name='user_dashboard'),
    path('login', views.sign_in, name='login_user'),
    path('logout', LogoutView.as_view(next_page='/'), name='logout'),
    path('users', views.list_registered_users, name='system_users'),
    path('activate/user/<int:user_id>', views.user_activate, name='activate_user'),
    path('deactivate/user/<int:user_id>', views.user_deactivate, name='deactivate_user'),
]
