from django.shortcuts import render, redirect
from app.forms import HeroForm, AboutForm
from app.models import HeroModel, AboutModel

# Create your views here.
def index(request):
    heroModel = HeroModel.objects.all()
    aboutModel = AboutModel.objects.all()
    return render(request, 'app/index.html', {"heroModel": heroModel, "aboutModel": aboutModel})

def backoffice(request):
    heroModel = HeroModel.objects.all()
    aboutModel = AboutModel.objects.all()
    return render(request, 'app/backoffice/backoffice.html', {"heroModel": heroModel, "aboutModel": aboutModel})

def menuModif(request):
    return render(request, 'app/backoffice/menuModif.html')

def heroUpdate(request, id):
    edit = HeroModel.objects.get(id=id)
    if request.method == "POST":
        heroForm = HeroForm(request.POST, instance=edit)
        if heroForm.is_valid():
            heroForm.save()
            return redirect("backoffice")
    else: 
        heroForm = HeroForm(instance=edit)
    return render(request, 'app/backoffice/heroUpdate.html', {"heroForm": heroForm})

def aboutUpdate(request, id):
    edit = AboutModel.objects.get(id=id)
    if request.method == "POST":
        aboutForm = AboutForm(request.POST, instance=edit)
        if aboutForm.is_valid():
            aboutForm.save()
            return redirect("backoffice")
    else: 
        aboutForm = AboutForm(instance=edit)
    return render(request, 'app/backoffice/aboutUpdate.html', {"aboutForm": aboutForm})
