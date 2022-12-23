from django.forms import ModelForm
from . models import Message, Profile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
        }


class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = '__all__'
        exclude = ['sender', 'receipient', 'is_read']


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user', 'created']
