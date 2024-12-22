from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'first-task', FirstTaskViewSet, basename='first-task')
router.register(r'second-task', FirstTaskViewSet, basename='second-task')
router.register(r'third-task', FirstTaskViewSet, basename='third-task')
router.register(r'fourth-task', FirstTaskViewSet, basename='fourth-task')
router.register(r'sample', SampleViewSet, basename='sample')

urlpatterns = [
    path('', include(router.urls))
]