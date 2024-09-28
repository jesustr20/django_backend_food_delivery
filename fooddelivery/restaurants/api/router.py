from django.urls import path
from restaurants.api.views import (
    RestaurantCreateView,
    RestaurantListView,
    RestaurantDeleteView,
    RestaurantUpdateView,
    RestaurantDetailView
)

urlpatterns = [
    path('create/', RestaurantCreateView.as_view(), name='restaurant-create'),
    path('list/', RestaurantListView.as_view(), name='restaurant-list'),
    path('<int:pk>/detail/', RestaurantDeleteView.as_view(), name='restaurant-detail'),
    path('<int:pk>/update/', RestaurantUpdateView.as_view(), name='restaurant-update'),
    path('<int:pk>/delete/', RestaurantDetailView.as_view(), name='restaurant-delete'),
]