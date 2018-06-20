from django import forms

class userForm(forms.Form):
    username = forms.CharField(max_length=100)
