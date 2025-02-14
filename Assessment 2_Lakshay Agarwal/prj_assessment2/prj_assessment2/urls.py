from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('q1a/',include('app_q1a.urls')),
    path('q2/',include('app_q2.urls')),
]
