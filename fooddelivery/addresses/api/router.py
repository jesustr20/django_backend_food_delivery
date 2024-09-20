from django.urls import path
from addresses.api.views import (
    AddressCreateView,
    AddressListView,
    AddressDetailView,
    AddressUpdateView,
    AddressDeleteView,    
)

urlpatterns = [
    path('create/', AddressCreateView.as_view(), name='address-create'),
    path('list/', AddressListView.as_view(), name='address-list'),
    path('<int:pk>/detail/', AddressDetailView.as_view(), name='address-detail'),
    path('<int:pk>/update/', AddressUpdateView.as_view(), name='address-update'),
    path('<int:pk>/delete/', AddressDeleteView.as_view(), name='address-delete')
]