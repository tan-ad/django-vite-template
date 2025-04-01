from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # You can add customizations here if needed later
    model = CustomUser
    # Example: Add custom fields to the list display
    # list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'date_of_birth')

admin.site.register(CustomUser, CustomUserAdmin)
