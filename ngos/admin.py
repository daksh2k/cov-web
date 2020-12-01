from django.contrib import admin
from .models import Ngos

class NgosAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'is_verified', 'registration_no', 'phone') #What to display on admin table
    list_display_links = ('id', 'name', 'registration_no')
    list_editable = ('is_verified',)
    search_fields = ('name', 'email', 'registration_no')
    list_per_page = 25

admin.site.register(Ngos, NgosAdmin)
