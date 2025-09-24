from django.contrib.auth import login
from django.core import cache
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import (
    CreateView,
    DetailView,
    UpdateView,
    ListView,
)

from users.forms import UserRegisterForm, UserUpdateForm, UserBlockedForm
from users.models import User


class UserCreateView(CreateView):
    template_name = "users/register.html"
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users:login")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = "Добро пожаловать в наш сервис"
        message = "Спасибо, что зарегистрировались в нашем сервисе!"
        from_email = "Sasha.kel-1@yandex.ru"
        recipient_list = [user_email]
        send_mail(subject, message, from_email, recipient_list)


@method_decorator(cache_page(60 * 15), name="dispatch")
class UserDetailView(DetailView):
    template_name = "users/user_detail.html"
    model = User
    context_object_name = "user"


class UserUpdateView(UpdateView):
    template_name = "users/user_update.html"
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy("mailings:home_page")


class UsersListView(ListView):
    model = User
    template_name = "users/users_list.html"
    context_object_name = "users"

    def get_queryset(self):
        queryset = cache.get("users_list_view")
        if not queryset:
            queryset = super().get_queryset()
            cache.set("users_list_view", queryset, 60 * 15)


class UsersBlockedView(UpdateView):
    model = User
    template_name = "users/user_blocked.html"
    form_class = UserBlockedForm
    success_url = reverse_lazy("users:users_list")
