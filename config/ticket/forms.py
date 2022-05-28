from django import forms
from ticket.models import Ticket

class TicketForm(forms.ModelForm):
    
    title = forms.CharField(label="Title",max_length=128,widget=forms.TextInput())
    description = forms.CharField(label="Description",max_length=2048,widget=forms.Textarea(),required=False)
    image = forms.ImageField(label="Image",required=False)

    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']



