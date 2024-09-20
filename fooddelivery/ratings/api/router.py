from django.urls import path
from ratings.api.views import (
    RatingCreateView,
    RatingListView,
    RatingDetailView,
    RatingUpdateView,
    RatingDeleteView,
)

urlpatterns = [
    path('create/', RatingCreateView.as_view(), name='rating-create'),
    path('list/', RatingListView.as_view(), name='rating-list'),
    path('<int:pk>/detail/', RatingDetailView.as_view(), name='rating-detail'),
    path('<int:pk>/update/', RatingUpdateView.as_view(), name='rating-update'),
    path('<int:pk>/delete/', RatingDeleteView.as_view(), name='rating-delete'),
]