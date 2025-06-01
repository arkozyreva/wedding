from django.urls import path
from . import views

urlpatterns = [
    path('', views.wedding_invite, name='wedding_invite'),
    path('thank_you/', views.thank_you, name='thank_you'),
]
