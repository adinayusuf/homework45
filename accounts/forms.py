from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField


class MyUserCreationForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].required = True

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')

    def is_valid(self):
        super().is_valid()
        data = self.cleaned_data
        if not data.get('first_name') and not data.get('last_name'):
            self.add_error('first_name', 'One of the First Name or Last Name fields must be filled in')
            return False
        return True

# class MyUserCreationForm(forms.ModelForm):
#     password_confirm = forms.CharField(label='Enter your password again', widget=forms.PasswordInput,
#                                        strip=False)
#     password = forms.CharField(label='Enter your password', widget=forms.PasswordInput,
#                                strip=False)
#
#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get('password')
#         password_confirm = cleaned_data.get('password_confirm')
#         if password != password_confirm:
#             raise ValidationError('The passwords didnt match')
#         return cleaned_data
#
#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.set_password(self.cleaned_data.get('password'))
#         if commit:
#             user.save()
#         return user
#
#     class Meta:
#         model = User
#         fields = ['username', 'password', 'password_confirm', 'email', 'first_name', 'last_name']
