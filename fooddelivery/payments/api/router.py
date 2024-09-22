from django.urls import path
from payments.api.views import(
    PaymentCreateView,
    PaymentListView,
    PaymentDetailView,
    PaymentUpdateView,
    PaymentDeleteView
)

urlpatterns = [
    path('create/', PaymentCreateView.as_view(), name='payment-create'),
    path('list/', PaymentListView.as_view(), name='payment-list'),
    path('<int:pk>/detail/', PaymentDetailView.as_view(), name='payment-detail'),
    path('<int:pk>/update/', PaymentUpdateView.as_view(), name='payment-update'),
    path('<int:pk>/delete/', PaymentDeleteView.as_view(), name='payment-delete'),
]