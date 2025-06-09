from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
                 ("Information complémentaires", {"fields": ("description",)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            "fields": (
                'username', 'description', 'email', 'password1', 'password2',
                'is_staff', 'is_active', 'groups', 'user_permissions', 'is_superuser'
            )
        })
    )


admin.site.register(CustomUser, CustomUserAdmin)
