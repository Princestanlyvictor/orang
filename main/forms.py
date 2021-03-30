from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models.fields import files
from .models import userDetail
from .models import address
from django.forms import ModelForm

class userForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class accountform(ModelForm):
    class Meta:
        model = userDetail
        fields = ['mobile_number', 'address']


