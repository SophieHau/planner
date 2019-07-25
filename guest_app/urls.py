from django.urls import path
from . import views

app_name = 'guest_app'

urlpatterns = [
    path('guests/', views.get_guests, name='get_guests'),
]