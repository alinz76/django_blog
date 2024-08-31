from django.urls import path
from django.contrib.auth import views as auth_views
from . import views, forms


urlpatterns = [
    path('register/', views.register, name='user-register'),
    path('login/', views.UserLoginView.as_view(template_name='users/login.html', authentication_form=forms.LoginForm), name='user-login'),
    path('logout/', views.UserLogoutView.as_view(), name='user-logout'),
    path('profile/<str:username>/', views.profile, name='user-profile'),
]