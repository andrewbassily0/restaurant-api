from django.shortcuts import render , HttpResponse 
from rest_framework import viewsets , generics
from .models import Meal , Rating , User
from .serializers import MealSerializer, RatingSerilizer 

# Create your views here.
def index(request):
    return HttpResponse( ' hiiiii' )


class Meal_view(generics.ListCreateAPIView):
   queryset = Meal.objects.all()
   serializer_class = MealSerializer


class Meal_pk(generics.RetrieveDestroyAPIView):
   queryset = Meal.objects.all()
   serializer_class = MealSerializer