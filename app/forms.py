from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

from app.models import UserAccount


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        field_order = ('username','email','password1','password2')

    def save(self, commit=True):
        if not commit:
            raise NotImplementedError("Can't create User and UserAccount without database save")
        user = super(UserCreateForm, self).save(commit=True)
        user_account = UserAccount(user=user)
        user_account.save()

        return user, user_account
