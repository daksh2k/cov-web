from django import forms
from requirement.models import Requirement

class RequirementForm(forms.ModelForm):
  class Meta:
    model = Requirement
    fields = ['name', 'quantity', 'description', 'photo']