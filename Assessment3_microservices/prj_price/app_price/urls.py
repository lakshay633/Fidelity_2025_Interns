from django.urls import path,include
from .views import *
from rest_framework import routers
route = routers.DefaultRouter()
route.register(prefix='price',viewset=PriceViews,basename="base")

urlpatterns = [
    path('', include(route.urls)),
    path('loc/', get_loc),
]
