from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import STATUS_CHOICES


class ListForm(forms.Form):
    description = forms.CharField(max_length=100, required=True, label='Description',
                                  error_messages={"required":'Поле обязательно'},help_text="Введите заголовок")
    text = forms.CharField(max_length=3000, required=True, label='Text',
                           widget=widgets.Textarea(attrs={'cols': 20, 'rows': 5}))
    status = forms.ChoiceField(choices=STATUS_CHOICES, required=True, label='Status')
    date_of_completion = forms.DateField(label='Время создания', required=False,
                                         widget=widgets.DateInput(attrs={"type":"date"}))


    def clean_date_of_completion(self):
        if self.cleaned_data.get("date_of_completion") and self.cleaned_data.get("date_of_completion") < date.today():
            raise ValidationError("Дата публикации не должна быть раньше чем сегодня ")

    def clean(self):
        pass