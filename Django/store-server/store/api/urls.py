from rest_framework import routers
from django.urls import path, include
from api.views import ProductModelViewSet


app_name = 'api'

router = routers.DefaultRouter()
router.register(r'products', ProductModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]





