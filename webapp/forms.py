from django.forms import ModelForm

from webapp.models import ToDoList
from django.forms import CheckboxSelectMultiple, Textarea


class ListForm(ModelForm):
    class Meta:
        model = ToDoList
        exclude = ["created_at", "updated_at"]
        widgets = {'types': CheckboxSelectMultiple, 'description': Textarea(attrs={"rows": 1, "cols": 24})}