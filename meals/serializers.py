from rest_framework import serializers      
from . models import Meal, Rating  
from django.contrib.auth.models import User

class MealSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = '__all__'


class RatingSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

