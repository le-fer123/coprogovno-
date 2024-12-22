from rest_framework import serializers

from toefl.models import *


class FirstTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstTask
        fields = '__all__'


class SecondTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondTask
        fields = '__all__'


class ThirdTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThirdTask
        fields = '__all__'

class FourthTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = FourthTask
        fields = '__all__'


class TOEFLSampleSerializer(serializers.ModelSerializer):
    first = FirstTaskSerializer()
    second = SecondTaskSerializer()
    third = ThirdTaskSerializer()
    fourth = FourthTaskSerializer()

    class Meta:
        model = Sample
        fields = '__all__'
