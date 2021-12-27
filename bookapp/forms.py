from django.db import models
from django import forms
from .models import register_user, book_details
from django.contrib.auth.hashers import make_password
import re

class register_form(forms.ModelForm):
    name = forms.CharField(label='First name')
    username = forms.CharField(label='User name')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())
    repassword = forms.CharField(label='Retype password', widget=forms.PasswordInput())

    field_order = ['name', 'username', 'password', 'repassword']

    # def clean(self):
    #     cleaned_data = super().clean()
    #     pwd = self.cleaned_data['password']
    #     rpwd = self.cleaned_data['repassword']
    #     if pwd != rpwd:
    #         raise forms.ValidationError('Password mismatched!')
    #     return pwd
    def clean(self):
        cleaned_data = super(register_form, self).clean()
        username = self.cleaned_data['username']
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['repassword']
        if password != confirm_password:
            raise forms.ValidationError("password and confirm_password does not match")
        reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
        pat = re.compile(reg)
        mat = re.search(pat, password)
        if not mat:
            raise forms.ValidationError("Password invalid !!")
        if len(username)<5:
            raise forms.ValidationError("Enter username with length greater than 5 characters")
    class Meta:
        model = register_user
        fields = {'name', 'username', 'password'}

class BookDetails(forms.Form):
    class Meta:
        model = book_details
        fields = '__all__'

class login_form(forms.Form):
    user_name = forms.CharField(label='User name')
    password = forms.CharField(label='Password', widget=forms.PasswordInput())

    ordered_field_names = {'user_name', 'password'}
