from django import forms
from .models import HeroModel, AboutModel, SkillsModel, ContactModel, TestimonialsModel

class HeroForm(forms.ModelForm):
    class Meta:
        model = HeroModel
        fields = "__all__"
        
class AboutForm(forms.ModelForm):
    class Meta:
        model = AboutModel
        fields = "__all__"
        
class SkillsForm(forms.ModelForm):
    class Meta :
        model = SkillsModel
        fields = "__all__"
        
class ContactForm(forms.ModelForm):
    class Meta :
        model = ContactModel
        fields = "__all__"
        
class TestimonialsForm(forms.ModelForm):
    class Meta :
        model = TestimonialsModel
        fields = "__all__"