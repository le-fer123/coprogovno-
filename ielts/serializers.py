from rest_framework import serializers
from .models import *

class FirstPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = FirstPart
        fields = '__all__'

class SecondPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = SecondPart
        fields = '__all__'

class ThirdPartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ThirdPart
        fields = '__all__'

class IELTSSampleSerializer(serializers.ModelSerializer):
    first = FirstPartSerializer()
    second = SecondPartSerializer()
    third = ThirdPartSerializer()

    class Meta:
        model = Sample
        fields = '__all__'
