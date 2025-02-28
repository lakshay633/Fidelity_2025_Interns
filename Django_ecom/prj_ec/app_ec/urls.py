from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViews, product_list

router = DefaultRouter()
router.register(r'prod', ProductViews, basename="product")

urlpatterns = [
    path('', include(router.urls)),
    path('products/', product_list, name='product-list'),
]
