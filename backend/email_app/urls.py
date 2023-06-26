from django.urls import path

from email_app import views

urlpatterns = [
    path('accounts/reset_password/', views.reset_password)
    
]