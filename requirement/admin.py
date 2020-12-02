from django.contrib import admin
from .models import Requirement

class RequirementAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'quantity', 'ngos', 'is_satisfied') #What to display on admin table
  list_display_links = ('id', 'name')
  list_editable = ('is_satisfied',)
  search_fields = ('name', 'ngos')
  list_per_page = 25

admin.site.register(Requirement, RequirementAdmin)
