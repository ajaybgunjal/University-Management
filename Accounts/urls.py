from django.urls import path, include
from . import views
app_name = 'Accounts'

urlpatterns = [
    path('register/', views.user_registration, name = 'register'),
]