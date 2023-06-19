from django.urls import path

from email_app import views

urlpatterns = [
    path('reset_password/', views.ResetPasswordEmail),
    
]