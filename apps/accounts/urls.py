from django.urls import path

from apps.accounts.views import dashboard_view, login_view

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('', dashboard_view, name='dashboard'),
]
