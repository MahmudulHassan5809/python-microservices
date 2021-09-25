from django.urls import path,include
from rest_framework.routers import DefaultRouter

from products import views

router = DefaultRouter()

router.register('products',views.ProductViewSet)

app_name = 'products'

urlpatterns = [
    path('',include(router.urls))
]