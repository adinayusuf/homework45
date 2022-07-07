from datetime import date

from django import forms
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import ToDoList


class ListForm(ModelForm):
    class Meta:
        model = ToDoList
        fields = '__all__'