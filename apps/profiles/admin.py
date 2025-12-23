from django.contrib import admin

# Register your models here.
from .models import Profile


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'pkid', 'user', 'gender', 'phone_number', 'country', 'city')
    list_filter = ('country', 'gender', 'city')
    search_fields = ('user__username', 'city', 'country', 'phone_number')
    list_display_links = ('id', 'pkid', 'user')

admin.site.register(Profile, ProfileAdmin)