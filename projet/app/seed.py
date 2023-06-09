from django_seed import Seed
from .models import HeroModel, AboutModel, SkillsModel

def run():
    seeder = Seed.seeder()

    seeder.add_entity(HeroModel, 1, {
        "prenom" : "Alex",
        "nom" : "Smith",
    })
    
    seeder.add_entity(AboutModel, 1, {
        "picture" : "img/profile-img.jpg",
        "intro": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
        "job" : "UI/UX Designer & Web Developer.",
        "birthday" : "1 May 1995",
        "website" : "www.example.com",
        "phone" : "+123 456 7890",
        "city" : "New York, USA",
        "age" : 30,
        "degree" : "Master",
        "email" : "email@example.com",
        "freelance" : "Available",
        "description" : "Officiis eligendi itaque labore et dolorum mollitia officiis optio vero. Quisquam sunt adipisci omnis et ut. Nulla accusantium dolor incidunt officia tempore. Et eius omnis. Cupiditate ut dicta maxime officiis quidem quia. Sed et consectetur qui quia repellendus itaque neque. Aliquid amet quidem ut quaerat cupiditate. Ab et eum qui repellendus omnis culpa magni laudantium dolores.",
    })
    
    datas = [
        { "skill": "HTML", "value": 100 },
        { "skill": "CSS", "value": 90 },
        { "skill": "JavaScript", "value": 75 },
        { "skill": "PHP", "value": 80 },
        { "skill": "WordPress/CMS", "value": 90 },
        { "skill": "Photoshop", "value": 55 }
    ]

    for i in datas:
        seeder.add_entity(SkillsModel, 1, i)

    seeder.execute()
    print("Datas _about OK !")