from django.contrib import admin
from .models import User


class UserAdminTest(admin.ModelAdmin):
    list_display = ['username', 'email', 'date_joined']


admin.site.register(User, UserAdminTest)

