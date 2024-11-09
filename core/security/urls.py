from django.urls import path
from core.security.views import auth

app_name = "security"

urlpatterns = [
    path('login/', auth.AdminLoginView.as_view(), name='login'),
    path('logout/', auth.Admin_Logout, name='logout')
]