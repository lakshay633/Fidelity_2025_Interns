from django.urls import path,include
from .views import *
from rest_framework import routers
route = routers.DefaultRouter()
route.register(prefix='trip',viewset=TripViews,basename="base")

urlpatterns = [
    path('', include(route.urls)),
    path('duration/', TripViews.as_view({'get': 'duration'}), name='trip-duration'),
    path('gbd/<str:tripDate>/', TripViews.as_view({'get': 'getByDate'}), name='trip-by-date'),
]
