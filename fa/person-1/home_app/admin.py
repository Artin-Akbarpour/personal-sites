from django.contrib import admin
from . import models
import django_jalali.admin as jadmin

class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'birth_date')
    jdate_fields = ('created_at',)  # مشخص کردن فیلدهای تاریخ شمسی

admin.site.register(models.person, PostAdmin)
