from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

from inmuebles import views

router = DefaultRouter()
router.register(r'inmuebles', views.InmueblesViewSet, basename='inmuebles')

app_name = 'inmuebles'

urlpatterns = [
    path('', include(router.urls))
]
