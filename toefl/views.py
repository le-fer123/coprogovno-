from rest_framework import viewsets
from .serializers import *


class FirstTaskViewSet(viewsets.ModelViewSet):
    queryset = FirstTask.objects.all()
    serializer_class = FirstTaskSerializer


class SecondTaskViewSet(viewsets.ModelViewSet):
    queryset = SecondTask.objects.all()
    serializer_class = SecondTaskSerializer


class ThirdTaskViewSet(viewsets.ModelViewSet):
    queryset = ThirdTask.objects.all()
    serializer_class = ThirdTaskSerializer


class FourthTaskViewSet(viewsets.ModelViewSet):
    queryset = FourthTask.objects.all()
    serializer_class = FourthTaskSerializer


class SampleViewSet(viewsets.ModelViewSet):
    queryset = Sample.objects.all()
    serializer_class = TOEFLSampleSerializer
