from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .forms import CustomeUserChangeForm,CustomUserCreationForm
from .models import CustomUser

# Register your models here.

class CustomeUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomeUserChangeForm
    model = CustomUser
    list_display = ['email', 'username']

admin.site.register(CustomUser, CustomeUserAdmin)