from django.urls import path, include
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import *

schema_view = get_schema_view(
    openapi.Info(
        title="IELTS COPRO",
        default_version='v1',
        description="...",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register(r'sample', SampleViewSet, basename='sample')
router.register(r'firstpart', FirstPartViewSet, basename='firstpart')
router.register(r'secondpart', SecondPartViewSet, basename='secondpart')
router.register(r'thirdpart', ThirdPartViewSet, basename='thirdpart')

urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('', include(router.urls)),
    path('answer/', AnswerUploadView.as_view(), name="answer-upload"),
    path('question/', QuestionView.as_view(), name="question-upload")
]
