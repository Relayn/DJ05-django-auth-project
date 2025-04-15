from django.urls import path
from .views import HomeView, ProfileView, RegisterView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', HomeView.as_view(), name='home'),  # Главная страница
    path('profile/', ProfileView.as_view(), name='profile'),  # Страница профиля
    path('register/', RegisterView.as_view(), name='register'),  # Страница регистрации
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),  # Страница входа
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),  # Выход
]