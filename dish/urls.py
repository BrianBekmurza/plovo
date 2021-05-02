from django.urls import path
from .views import DishListAPIView

app_name = 'dish'

urlpatterns = [
    path('dish/', DishListAPIView.as_view(), name='dishes'),
]