# from django import forms
# from tg_couchman.models import Project
# from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# from django.forms.widgets import PasswordInput, TextInput



# class Projectform(forms.ModelForm):     
#     class Meta:
#         model = Project
#         fields = '__all__'

# class CreateUserForm(UserCreationForm):
#     class Meta:
#        model = User
#        fields = ['username', 'password1', 'password2'] 
        
# class LoginForm(AuthenticationForm):
#     username = forms.CharField(widget=TextInput())
#     password = forms.CharField(widget=PasswordInput())