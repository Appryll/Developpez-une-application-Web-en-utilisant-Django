from django import forms
from review.models import Review

class ReviewForm(forms.ModelForm):
    headline = forms.CharField(label="Title",max_length=128,widget=forms.TextInput())
    rating = forms.ChoiceField(initial=1, label="Note", widget=forms.RadioSelect(),
        choices=((1, " - 1 "), (2, " - 2 "), (3, " - 3 "), (4, ' - 4 '), (5, ' - 5 ')))
    body = forms.CharField(label="Commentaire", max_length=8192, widget=forms.Textarea(),required=False)

    class Meta:
        model = Review
        fields = ['headline', 'rating', 'body']