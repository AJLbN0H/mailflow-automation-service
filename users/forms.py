from django.contrib.auth.forms import UserCreationForm
from django import forms
from users.models import User


class UserRegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = ["email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите Email"}
        )
        self.fields["password1"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Введите пароль"}
        )
        self.fields["password2"].widget.attrs.update(
            {"class": "form-control", "placeholder": "Повторите введенный пароль"}
        )


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["email", "avatar", "phone", "country"]

    def __init__(self, *args, **kwargs):
        super(UserUpdateForm, self).__init__(*args, **kwargs)
        self.fields["email"].widget.attrs.update({"class": "form-control"})
        self.fields["avatar"].widget.attrs.update({"class": "form-control"})
        self.fields["phone"].widget.attrs.update({"class": "form-control"})
        self.fields["country"].widget.attrs.update({"class": "form-control"})


class UserBlockedForm(forms.ModelForm):

    class Meta:
        model = User
        fields = [
            "is_active",
        ]

    def __init__(self, *args, **kwargs):
        super(UserBlockedForm, self).__init__(*args, **kwargs)
        self.fields["is_active"].widget.attrs.update({"class": "form-check"})
