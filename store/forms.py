from django import forms

class SearchForm(forms.Form):
    text = forms.CharField(label='поиск', max_length=100)