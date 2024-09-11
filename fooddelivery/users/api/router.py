from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.api.views import (
    UserCreateView,
    UserDetailView,
    UserUpdateView,
    UserDeleteView,
    UserListView,
    PasswordResetRequestView,
    PasswordResetConfirmView
)


urlpatterns = [    
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
    path('password_reset/request', PasswordResetRequestView.as_view(), name='password-reset-request'),
    path('password_reset/confirm', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

