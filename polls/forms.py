# Django imports
from django import forms
# Local imports
from .models import Poll, Vote


class PollForm(forms.ModelForm):
    class Meta:
        model = Poll
        fields = ['question', 'allow_anon', 'allow_result']
        widgets = {
            'question': forms.TextInput(attrs={'class': 'forms-group__input'})
        }


class VoteForm(forms.ModelForm):
    class Meta:
        model = Vote
        fields = ['vote']
        #widgets = {
        #    'question': forms.TextInput(attrs={'class': 'forms-group__input'})
        #}