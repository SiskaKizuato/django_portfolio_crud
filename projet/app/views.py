from django.shortcuts import render, redirect
from app.forms import HeroForm, AboutForm, SkillsForm, ContactForm, TestimonialsForm
from app.models import HeroModel, AboutModel, SkillsModel, ContactModel, TestimonialsModel

# Create your views here.
def index(request):
    heroModel = HeroModel.objects.all()
    aboutModel = AboutModel.objects.all()
    skillsModel = SkillsModel.objects.all()
    contactModel = ContactModel.objects.all()
    testimonialsModel = TestimonialsModel.objects.all()
    return render(request, 'app/index.html', {"heroModel": heroModel, "aboutModel": aboutModel, "skillsModel": skillsModel, "contactModel":contactModel, "testimonialsModel":testimonialsModel})

def backoffice(request):
    heroModel = HeroModel.objects.all()
    aboutModel = AboutModel.objects.all()
    skillsModel = SkillsModel.objects.all()
    contactModel = ContactModel.objects.all()
    testimonialsModel = TestimonialsModel.objects.all()
    return render(request, 'app/backoffice/backoffice.html', {"heroModel": heroModel, "aboutModel": aboutModel, "skillsModel": skillsModel, "contactModel": contactModel, "testimonialsModel":testimonialsModel})

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

def contactUpdate(request, id):
    edit = ContactModel.objects.get(id=id)
    if request.method == "POST":
        contactForm = ContactForm(request.POST, instance=edit)
        if contactForm.is_valid():
            contactForm.save()
            return redirect("backoffice")
    else: 
        contactForm = ContactForm(instance=edit)
    return render(request, 'app/backoffice/contactUpdate.html', {"contactForm": contactForm})

def toCreateSkill(request):
    skillsModel = SkillsModel.objects.all()
    return render(request, "app/backoffice/toCreateSkill.html", { "skillsModel": skillsModel })

def toCreateTestimonials(request):
    testimonialsModel = TestimonialsModel.objects.all()
    return render(request, "app/backoffice/toCreateTestimonials.html", { "testimonialsModel": testimonialsModel })


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

def testimonialsEdit(request, id):
    edit = TestimonialsModel.objects.get(id=id)
    if request.method == "POST":
        testimonialsForm = TestimonialsForm(request.POST, instance=edit)
        if testimonialsForm.is_valid():
            testimonialsForm.save()
            return redirect("toCreateTestimonials")
    else: 
        testimonialsForm = TestimonialsForm(instance=edit)
    return render(request, 'app/backoffice/testimonialsEdit.html', {"testimonialsForm": testimonialsForm})

def skillDestroy(request, id):
    destroy = SkillsModel(id)
    destroy.delete()
    return redirect("toCreateSkill")

def testimonialsDestroy(request, id):
    destroy = TestimonialsModel(id)
    destroy.delete()
    return redirect("toCreateTestimonials")

def skillAdd(request):
    if request.method=="POST":
        skillForm = SkillsForm(request.POST)
        if skillForm.is_valid():
            skillForm.save()
            return redirect("toCreateSkill")
    else : 
        skillForm=SkillsForm()
    return render(request, 'app/backoffice/skillAdd.html', {"skillForm": skillForm})

def testimonialsAdd(request):
    if request.method=="POST":
        testimonialsForm = TestimonialsForm(request.POST)
        if testimonialsForm.is_valid():
            testimonialsForm.save()
            return redirect("toCreateTestimonials")
    else : 
        testimonialsForm=TestimonialsForm()
    return render(request, 'app/backoffice/testimonialsAdd.html', {"testimonialsForm": testimonialsForm})