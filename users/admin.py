from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class CustomUserAdmin(UserAdmin):

    readonly_fields = ("date_joined", "last_login", "updated_at")

    fieldsets = (
        ("Credentials", {"fields": ("username", "password")}),
        (
            "Personal Info",
            {"fields": ("email", "first_name", "last_name", "birthdate", "bio")},
        ),
        (
            "Permissions",
            {"fields": ("is_critic", "is_superuser", "is_active", "is_staff")},
        ),
        ("Important Dates", {"fields": ("date_joined", "last_login", "updated_at")}),
    )


admin.site.register(User, CustomUserAdmin)
