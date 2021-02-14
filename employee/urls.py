from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('employees', views.EmployeeView)
router.register('offices', views.OfficeView)
router.register('visitors', views.VisitorView)

urlpatterns = [
    path('', views.index, name='index'),
    path('employees/', views.employees, name='employees'),
    path('api/', include(router.urls)),
]
