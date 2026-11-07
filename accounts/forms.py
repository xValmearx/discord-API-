from django.contrib.auth.forms import (
    UserChangeForm,
    UserCreationForm,
)

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """Form used to create a new user."""

    class Meta:
        model = CustomUser

        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
        )


class CustomUserChangeForm(UserChangeForm):
    """Form used to edit an existing user."""

    class Meta:
        model = CustomUser

        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "date_of_birth",
        )