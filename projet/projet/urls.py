"""
URL configuration for azz project.

The  list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('backoffice', views.backoffice, name="backoffice"),
    path('menuModif', views.menuModif, name="menuModif"),
    path('heroUpdate/<int:id>', views.heroUpdate, name="heroUpdate"),
    path('aboutUpdate/<int:id>', views.aboutUpdate, name="aboutUpdate"),
    path('contactUpdate/<int:id>', views.contactUpdate, name="contactUpdate"),
    path('toCreateSkill', views.toCreateSkill, name="toCreateSkill"),
    path('toCreateTestimonials', views.toCreateTestimonials, name="toCreateTestimonials"),
    path('skillEdit/<int:id>', views.skillEdit, name="skillEdit"),
    path('testimonialsEdit/<int:id>', views.testimonialsEdit, name="testimonialsEdit"),
    path('skillDestroy/<int:id>', views.skillDestroy, name="skillDestroy"),
    path('testimonialsDestroy/<int:id>', views.testimonialsDestroy, name="testimonialsDestroy"),
    path('skillAdd/', views.skillAdd, name="skillAdd"),
    path('testimonialsAdd/', views.testimonialsAdd, name="testimonialsAdd"),
]
