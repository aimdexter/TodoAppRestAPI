from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.html import format_html
from django.utils.translation import gettext_noop as _

from .models import User  # Adjust this import according to your application structure


class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Personal info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "avatar",
                    "phone",
                    "address",
                    "city",
                    "state",
                    "country",
                    "tz",
                    "region",
                    "zip",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
        (_("Social"), {"fields": ("github", "linked_in", "stack_overflow", "twitter")}),
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
                    "first_name",
                    "last_name",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )

    def avatar_tag(self, obj):
        if obj.avatar:
            return format_html(
                '<img src="{}" style="width:50px; height:50px; border-radius: 50% "/>'.format(
                    obj.avatar.url
                )
            )
        else:
            return "No avatar uploaded"

    avatar_tag.short_description = "Avatar image"

    list_display = (
        "email",
        "first_name",
        "last_name",
        "is_active",
        "is_staff",
        "is_superuser",
        "avatar_tag",
    )
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email",)


admin.site.register(User, UserAdmin)
