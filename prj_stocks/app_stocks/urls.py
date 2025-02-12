from django.contrib import admin
from django.urls import path
from .views import *

# Define namespace for this app

urlpatterns = [
    path('', Myclass.as_view(), name='home'),
    path('login/', loginPage , name='login'),
    path('register/', registerPage , name='register'),
    path('show/',StockList.as_view(),name='show'),
    path('create/',StockCreate.as_view(),name='create'),
    path('update/<int:pk>',StockUpdate.as_view(),name='update'),
    path('delete/<int:pk>',StockDelete.as_view(),name='delete')

]
