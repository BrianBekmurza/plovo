from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Dish
from .serializers import *


class DishListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        dishes = Dish.objects.order_by('name')
        dishes_serialized = DishListSerializer(dishes, many=True)
        return Response(data=dishes_serialized.data)


class DishCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.POST
        serializer = DishCreateSerializer(data=data)
        if serializer.is_valid():
            dish_object = serializer.save()
            return Response(data={'message': 'Блюдо успешно создано'})

class DishUpdateAPIView(APIView):
    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        dish = Dish.objects.get(pk=pk)

        data = request.POST
        serializer = DishUpdateAPIView(data=data)

        if serializer.is_valid():
            dish.name = serializer.validated_data.get('name')
            dish.price = serializer.validated_data.get('price')
            dish.save()
            serialized_object = DishSerializer(dish)
            data = serialized_object.data
            return Response(data=data)
        return Response(data=serializer.errors)

class DishDetailAPIView(APIView):
    def get(self, request, *args, **kwargs):
        dish_object = Dish.objects.get(pk=kwargs.get('pk'))
        serializer = DishSerializer(instance=dish_object)
        return Response(data=serializer.data)


class DishDeleteAPIView(APIView):
    def delete(self, request, *args, **kwargs):
        dish = Dish.objects.get(pk=kwargs.get('pk'))
        dish.delete()
        return Response(data={'message': 'Блюдо было удалено'})
