from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):
    template_name = 'main/home.html'  # Главная страница

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'main/profile.html'  # Страница профиля, только для авторизованных
    login_url = reverse_lazy('login')    # Редирект на вход, если не авторизован

class RegisterView(CreateView):
    form_class = UserCreationForm        # Форма регистрации
    template_name = 'main/register.html' # Шаблон регистрации
    success_url = reverse_lazy('login')  # Редирект на страницу входа после регистрации