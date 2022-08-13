from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from webapp.models import ToDoList, Project, ProjectUser
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


class MemberAddForm(forms.ModelForm):
    class Meta:
        model = ProjectUser
        fields = ['user', 'role']

    def __init__(self, *args, **kwargs):
        project_id = kwargs.pop('project_id', None)
        super().__init__(*args, **kwargs)
        members = ProjectUser.objects.filter(project_id=project_id).values_list('user_id', flat=True)
        if project_id:
            self.fields['user'].queryset = User.objects.exclude(id__in=members)