from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class UserForm(UserCreationForm):
#    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
#    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    choices = (("dept1", "dept1"), ("dept2", "dept2") )
    designation_choices = (("Admin", "Admin"), ("Employee" , "Employee"))
    depatments_in_organization = forms.ChoiceField(help_text='Required. Select user department', choices=choices)
    designation = forms.ChoiceField(choices=designation_choices,required=True)
    class Meta:
        model = User
        fields = ['username', 'password1','password2', 'designation', 'depatments_in_organization']




