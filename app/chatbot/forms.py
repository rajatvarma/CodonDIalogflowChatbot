from django import forms

class NameForm(forms.Form):
    user_input = forms.CharField(label='Ask?', max_length=500)