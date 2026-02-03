from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.views import (
    UserCreateView,
    UserUpdateView,
    UserDetailView,
    UsersListView,
    UsersBlockedView,
)

app_name = "users"

urlpatterns = [
    path("login/", LoginView.as_view(template_name="users/login.html"), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", UserCreateView.as_view(), name="register"),
    path("profile_detail/<int:pk>/", UserDetailView.as_view(), name="user_detail"),
    path("profile_update/<int:pk>/", UserUpdateView.as_view(), name="user_update"),
    path("users_list/", UsersListView.as_view(), name="users_list"),
    path("user_blocked/<int:pk>/", UsersBlockedView.as_view(), name="user_blocked"),
]
