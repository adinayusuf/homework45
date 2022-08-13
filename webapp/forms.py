import re

from django.core.exceptions import ValidationError
from django import forms
from django.forms import ModelForm

from webapp.models import ToDoList, Project
from django.forms import CheckboxSelectMultiple, Textarea


class ListForm(ModelForm):
    class Meta:
        model = ToDoList
        exclude = ["created_at", "updated_at"]
        widgets = {'types': CheckboxSelectMultiple,
                   'description': Textarea(attrs={"rows": 1, "cols": 24})}


class SearchForm(forms.Form):
    search = forms.CharField(max_length=50, required=False, label='Find')


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['data_begin', 'data_end', 'title', 'description']
