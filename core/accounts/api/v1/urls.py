from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'api-v1'
urlpatterns = [
    # sign Up
    path('registration/', views.RegistrationApiView.as_view(), name='registration'),
    # login and logout
    path('token/login/', views.CustomObtainAuthToken.as_view(), name='token-login'),
    path('token/logout/', views.CustomDiscardAuthToken.as_view(), name='token-logout'),

    # change password
    path('change-password/', views.ChangePasswordApiView.as_view(), name='change-password'),

    # token creation
    path('jwt/create/', views.CustomTokenObtainPairView.as_view(), name='jwt-create'),
    path('jwt/refresh/', TokenRefreshView.as_view(), name='jwt-refresh'),

    # profile path
    path('profile/', views.ProfileApiView.as_view(), name='profile'),
]
