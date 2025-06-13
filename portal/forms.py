
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Communication

class CustomUserCreationForm(UserCreationForm):

    company_name = forms.CharField(max_length=255, required=True, label="Company Name")
    first_name = forms.CharField(max_length=150, required=True, label="First Name")
    last_name = forms.CharField(max_length=150, required=True, label="Last Name")
    email = forms.EmailField(required=True, label="Email Address")

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'company_name',)

class CommunicationForm(forms.ModelForm):
    class Meta:
        model = Communication
    
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs={
                'rows': 3, 
                'placeholder': 'Type your message here...'
                }),
        }
        labels = {
            'message': '' 
        }