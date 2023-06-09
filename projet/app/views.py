from django.shortcuts import render, redirect
from app.forms import HeroForm, AboutForm, SkillsForm
from app.models import HeroModel, AboutModel, SkillsModel

# Create your views here.
def index(request):
    heroModel = HeroModel.objects.all()
    aboutModel = AboutModel.objects.all()
    skillsModel = SkillsModel.objects.all()
    return render(request, 'app/index.html', {"heroModel": heroModel, "aboutModel": aboutModel, "skillsModel": skillsModel})

def backoffice(request):
    heroModel = HeroModel.objects.all()
    aboutModel = AboutModel.objects.all()
    skillsModel = SkillsModel.objects.all()
    return render(request, 'app/backoffice/backoffice.html', {"heroModel": heroModel, "aboutModel": aboutModel, "skillsModel": skillsModel})

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

def toCreateSkill(request):
    skillsModel = SkillsModel.objects.all()
    return render(request, "app/backoffice/toCreateSkill.html", { "skillsModel": skillsModel })


def skillEdit(request, id):
    edit = SkillsModel.objects.get(id=id)
    if request.method == "POST":
        skillsForm = SkillsForm(request.POST, instance=edit)
        if skillsForm.is_valid():
            skillsForm.save()
            return redirect("toCreateSkill")
    else: 
        skillsForm = SkillsForm(instance=edit)
    return render(request, 'app/backoffice/skillEdit.html', {"skillsForm": skillsForm})

def skillDestroy(request, id):
    destroy = SkillsModel(id)
    destroy.delete()
    return redirect("toCreateSkill")

def skillAdd(request):
    if request.method=="POST":
        skillForm = SkillsForm(request.POST)
        if skillForm.is_valid():
            skillForm.save()
            return redirect("toCreateSkill")
    else : 
        skillForm=SkillsForm()
    return render(request, 'app/backoffice/skillAdd.html', {"skillForm": skillForm})