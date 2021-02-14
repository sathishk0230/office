from django.urls import path, include
from . import views
urlpatterns = [
    path('employees/', views.employees, name='employees')
]
