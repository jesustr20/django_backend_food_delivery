from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.api.views import (
    UserCreateView,
    UserDetailView,
    UserUpdateView,
    UserDeleteView,
    UserListView,
    PasswordResetView,
    CodeVerificationView,
    PasswordChangeView
)


urlpatterns = [    
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', UserDeleteView.as_view(), name='user-delete'),
    path('password/reset/', PasswordResetView.as_view(), name='password-reset'),
    path('password/reset-verify/', CodeVerificationView.as_view(), name='password-reset-verify'),
    path('password/change/', PasswordChangeView.as_view(), name='password-change'),
    path('auth/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

