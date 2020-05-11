from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import CustomUserCreateForm, CustomUserChangeForm
from users.models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreateForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('first_name', 'last_name', 'phone', 'is_staff')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal data', {'fields': ('first_name', 'last_name', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Historical', {'fields': ('last_login', 'date_joined')})
    )
