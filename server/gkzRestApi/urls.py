from django.conf.urls import url, include 

from django.contrib import admin
from django.urls import path

from rest_framework.routers import DefaultRouter
from customers.views import CustomerViewSet


router = DefaultRouter()
router.register(prefix='customers', viewset=CustomerViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('admin/', admin.site.urls),
]