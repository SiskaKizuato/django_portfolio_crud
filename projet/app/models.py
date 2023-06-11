from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class HeroModel(models.Model):
    prenom = models.CharField(max_length=35)
    nom = models.CharField(max_length=35)

class AboutModel(models.Model):
    picture = models.CharField(max_length=700)
    # picture = models.URLField()
    intro = models.TextField()
    job = models.CharField(max_length=100)
    birthday = models.CharField(max_length=50)
    website = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    # phone = PhoneField(blank=True, help_text='Contact phone number')
    city = models.CharField(max_length=60)
    age = models.PositiveIntegerField()
    degree = models.CharField(max_length=20)
    email = models.EmailField()
    freelance = models.CharField(max_length=20)
    description = models.TextField()
    
class SkillsModel(models.Model):
    skill = models.CharField(max_length=30)
    value = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])
    
class ContactModel(models.Model):
    location = models.CharField(max_length=300)
    email = models.EmailField()
    call = models.CharField(max_length=50)
