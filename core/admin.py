from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User 


@admin.register(User)
class BaseUserAdmin(UserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2","subscriptiontype"),
            },
        ),
    )
    
