from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from real_estate_web_application.accounts.forms import CustomUserChangeForm, CustomUserCreationForm
from real_estate_web_application.accounts.models import Profile

UserModel = get_user_model()


@admin.register(UserModel)
class CustomUserModelAdmin(UserAdmin):
    model = UserModel
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm

    list_display = ("pk", "username", "is_staff", "is_superuser")
    ordering = ("pk",)

    fieldsets = (
        ("Credentials", {"fields": ("username", "password")}),
        ("Personal info", {"fields": ("first_name", "last_name", "email")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", )}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2"),
            },
        ),
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    list_filter = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name")
    ordering = ("last_name",)




