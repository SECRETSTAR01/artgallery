from django import forms
from .models import *

class ArtForm(forms.ModelForm):
    class Meta:
        model = ArtModel
        fields = ('art_work', 'title', 'artist')
