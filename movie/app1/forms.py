from django import forms

from app1.models import Movies


class MovieForm(forms.ModelForm):
    class Meta:
        model=Movies
        fields='__all__'