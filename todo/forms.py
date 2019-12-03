from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class TodoForm(forms.Form):
    title = forms.CharField(max_length=40,
                            widget= forms.TextInput(
                                attrs={'class': 'form-control', 'placeholder': 'Enter todo e.g. Delete junk files',
                                       'aria-label': 'Todo', 'aria-describedby': 'add-btn'}
                            ))

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(widget= forms.TextInput(
                                attrs={'class': 'form-control',
                                       'placeholder': "Email"
                                       }))

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control', 'placeholder': "Password"
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control', 'placeholder': "Password"
        })
        self.fields['username'].widget.attrs.update({
            'class': 'form-control', 'placeholder': "Username"
        })


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(widget= forms.TextInput(
                                attrs={'class': 'form-control'
                                       }))

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'})
        }