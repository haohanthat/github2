from django import forms
import re
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
    username=   forms.CharField(label='Tai khoan', max_length=30)
    emai=       forms.EmailField(label='Email')
    password1=  forms.CharField(label='Mat khau',widget=forms.PasswordInput())
    password2=  forms.CharField(label='Mat khau',widget=forms.PasswordInput())

    def clean_password2(self):
        if password1 in self.clean_data:
            password1= self.clean_data['password1']
            password2= self.clean_data['password2']
            if password1==password2 and password1:
                return password2
        raise forms.ValidationError("Mat khau khong hop le")
    
    def clean_username(self):
        username=self.clean_data['username']
        if not re.search(r,'^w+&',username):
            raise forms.ValidationError('Ten tai khoan co ki tu dac biet')
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.validationError('Tai khoan da ton tai')
    
    def save(self):
        User.objects.create_user(username=self.clean_data['username'],email=self.clean_data['email'],password=self.clean_data['password2'])

class login(forms.Form):
    username=   forms.CharField(label='Tai khoan', max_length=30)
    emai=       forms.EmailField(label='Email')
    password=  forms.CharField(label='Mat khau',widget=forms.PasswordInput())