from django.urls import path
from drivers.api.views import(
    DriverCreateView,
    DriverListView,
    DriverDetailView,
    DriverUpdateView,
    DriverDeleteView
)

urlpatterns = [
    path('create/', DriverCreateView.as_view(), name='driver-create'),
    path('list/', DriverListView.as_view(), name='driver-list'),
    path('<int:pk>/detail/', DriverDetailView.as_view(), name='driver-detail'),
    path('<int:pk>/update/', DriverUpdateView.as_view(), name='driver-update'),
    path('<int:pk>/delete/', DriverDeleteView.as_view(), name='driver-delete'),
]