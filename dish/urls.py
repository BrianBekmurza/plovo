from django.urls import path
from .views import DishListAPIView, DishDetailAPIView, DishUpdateAPIView, DishDeleteAPIView, DishCreateAPIView 

app_name = 'dish'

urlpatterns = [
    path('dish/', DishListAPIView.as_view(), name='dishes'),
    path('<int:pk>/', DishDetailAPIView.as_view(), name='dish'),
    path('<int:pk>/update/', DishUpdateAPIView.as_view(), name='update-dish'),
    path('<int:pk>/delete/', DishDeleteAPIView.as_view(), name='delete-dish'),
    path('create/', DishCreateAPIView.as_view(), name='create-dish'),
]