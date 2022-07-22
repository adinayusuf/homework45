import re

from django.core.exceptions import ValidationError
from django import forms
from django.forms import ModelForm

from webapp.models import ToDoList
from django.forms import CheckboxSelectMultiple, Textarea


class ListForm(ModelForm):
    class Meta:
        model = ToDoList
        exclude = ["created_at", "updated_at"]
        widgets = {'types': CheckboxSelectMultiple,
                   'description': Textarea(attrs={"rows": 1, "cols": 24})}

    def clean_summary(self):
        title = self.cleaned_data.get('summary')
        if len(title) > 25:
            raise ValidationError('Summary must be less 10 symbol')
        if not re.match('^[a-zA-Яа-я\s]+$', title):
            raise ValidationError('Enter only letters')
        return title

    def clean(self):
        if self.cleaned_data.get('summary') == self.cleaned_data.get('description'):
            raise ValidationError('Title and description cannot match')
        return super().clean()

    def clean_description(self):
        des = self.cleaned_data.get('description')
        if len(des) < 15:
            raise ValidationError('description is too short')
        return des


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label='Find')
