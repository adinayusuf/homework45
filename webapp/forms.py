from django import forms
from django.forms import widgets

from webapp.models import STATUS_CHOICES


class ListForm(forms.Form):
    description = forms.CharField(max_length=100, required=True, label='Description')
    text = forms.CharField(max_length=3000, required=True, label='Text',
                           widget=widgets.Textarea(attrs={'cols': 20, 'rows': 5}))
    status = forms.ChoiceField(choices=STATUS_CHOICES, label='Status')
    date_of_completion = forms.DateField(label='Время создания')
    update = forms.DateField(label='Время изменения')
