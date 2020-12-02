from django.contrib import admin
from .models import Donation

class DonationAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'quantity', 'users', 'ngos', 'is_completed') #What to display on admin table
  list_display_links = ('id', 'name')
  list_editable = ('is_completed',)
  search_fields = ('name', 'ngos', 'users')
  list_per_page = 25

admin.site.register(Donation, DonationAdmin)
