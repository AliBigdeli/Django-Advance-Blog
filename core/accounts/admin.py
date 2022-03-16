from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile


class CustomUserAdmin(UserAdmin):
    """
    Custom admin panel for user management with add and change forms plus password
    """

    model = User
    list_display = ("email", "is_superuser", "is_active", "is_verified")
    list_filter = ("email", "is_superuser", "is_active", "is_verified")
    searching_fields = ("email",)
    ordering = ("email",)
    fieldsets = (
        (
            "Authentication",
            {
                "fields": ("email", "password"),
            },
        ),
        (
            "permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "is_verified",
                ),
            },
        ),
        (
            "group permissions",
            {
                "fields": ("groups", "user_permissions"),
            },
        ),
        (
            "important date",
            {
                "fields": ("last_login",),
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "is_verified",
                ),
            },
        ),
    )


admin.site.register(Profile)
admin.site.register(User, CustomUserAdmin)
