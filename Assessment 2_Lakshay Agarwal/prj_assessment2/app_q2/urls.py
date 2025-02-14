from django.urls import path,include
from .views import *
from rest_framework import routers
route = routers.DefaultRouter()
route.register(prefix='pre',viewset=QuestionViews,basename="base")
# from rest_framework.schemas import get_schema_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# shema_view = get_schema_view(title="Student API")
shema_view = get_schema_view(openapi.Info(title="Question Papaer api",default_version="1.0.0",description = "std version", terms_of_service = "", contact= openapi.Contact(email="633lakshay@gmail.com"), license= openapi.License("Open")), public=True)

urlpatterns = [
    path('ques/', include(route.urls)),
    path('swagger/', shema_view.with_ui('swagger',cache_timeout=0)),
]
