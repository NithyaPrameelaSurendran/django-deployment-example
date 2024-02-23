from django import forms
from second_app.models import User

class New_User_Form(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'
        
        