from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Review  # Import the Review model

class CelebrantRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Add email field

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already in use.')
        return email
        
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['author_name', 'content']  # Clients will enter their name and review content
