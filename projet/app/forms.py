from django import forms
from .models import HeroModel, AboutModel

class HeroForm(forms.ModelForm):
    class Meta:
        model = HeroModel
        fields = "__all__"
        
class AboutForm(forms.ModelForm):
    class Meta:
        model = AboutModel
        fields = "__all__"