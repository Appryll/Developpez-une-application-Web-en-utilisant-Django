from django import forms
from ticket.models import Ticket

class TicketForm(forms.ModelForm):
    edit_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)
  
    class Meta:
        model = Ticket
        exclude = ['time_created', 'user']

class DeleteTicketForm(forms.Form):
    delete_ticket = forms.BooleanField(widget=forms.HiddenInput, initial=True)
