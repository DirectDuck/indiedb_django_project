from django import forms

class SearchForm(forms.Form):
    genre = forms.CharField()