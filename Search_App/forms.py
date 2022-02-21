from django import forms
from Search_App.models import SearchHis


class SearchForm(forms.ModelForm):
    keyword = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': '  Qtec Search'}))

    class Meta:
        model = SearchHis
        fields = ['keyword']
