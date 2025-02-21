from django.urls import path,include
from .views import *
from rest_framework import routers
route = routers.DefaultRouter()
route.register(prefix='loc',viewset=LocViews,basename="base")

urlpatterns = [
    path('', include(route.urls)),
]
