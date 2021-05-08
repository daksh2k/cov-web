from django import forms
from donation.models import Donation

class DonationForm(forms.ModelForm):
  class Meta:
    model = Donation
    fields = ['name', 'quantity', 'description', 'photo']