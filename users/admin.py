from django.contrib import admin
from .models import Users

class UsersAdmin(admin.ModelAdmin):
  list_display = ('id', 'first_name', 'last_name', 'email', 'phone') #What to display on admin table
  list_display_links = ('id', 'first_name', 'last_name')
  search_fields = ('first_name', 'last_name', 'email')
  list_per_page = 25

admin.site.register(Users, UsersAdmin)
