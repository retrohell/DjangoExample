from django import forms

class UsersForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(label='Description', max_length=200, required=False, widget=forms.Textarea(attrs={'class': 'input'}))

class ProjectsForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, widget=forms.TextInput(attrs={'class': 'input'}))
    description = forms.CharField(label='Description', max_length=200, required=False, widget=forms.Textarea(attrs={'class': 'input'}))
    