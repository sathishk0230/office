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
    path('employees/adde/', views.adde, name="adde"),
    path('api/', include(router.urls)),
    path('visitors/', views.visitors, name="visitors"),
    path('visitors/addv/', views.addv, name="addv"),
    path(r"^visitors/updatev/(?P<id>[0-9]+)/$", views.updatev, name="updatev"),
    path('register/', views.register, name='register')
]
