from django.urls import path,include
from .views import *
from rest_framework import routers
route = routers.DefaultRouter()
route.register(prefix='pre',viewset=PlanetViews,basename="base")

urlpatterns = [
    path('planet/', include(route.urls)),
]
