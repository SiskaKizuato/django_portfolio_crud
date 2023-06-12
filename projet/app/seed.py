from django_seed import Seed
from .models import HeroModel, AboutModel, SkillsModel, ContactModel, TestimonialsModel

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
        
    seeder.add_entity(ContactModel, 1, {
        "location": "A108 Adam Street, New York, NY 535022",
        "email": "info@example.com",
        "call": "+1 5589 55488 55"
    })
    
    datasTestimonials = [
        {
            "name": "Saul Goodman",
            "job": "Ceo Founder",
            "testimonial": "Proin iaculis purus consequat sem cure digni ssim donec porttitora entum suscipit rhoncus. Accusantium quam, ultricies eget id, aliquam eget nibh et. Maecen aliquam, risus at semper.",
            "picture": "static/app/img/testimonials/testimonials-1.jpg"
        },
        {
            "name": "Sara Wilsson",
            "job": "Designer",
            "testimonial": "Export tempor illum tamen malis malis eram quae irure esse labore quem cillum quid cillum eram malis quorum velit fore eram velit sunt aliqua noster fugiat irure amet legam anim culpa.",
            "picture": "static/app/img/testimonials/testimonials-2.jpg"
        },
        {
            "name": "Jena Karlis",
            "job": "Store Owner",
            "testimonial": "Enim nisi quem export duis labore cillum quae magna enim sint quorum nulla quem veniam duis minim tempor labore quem eram duis noster aute amet eram fore quis sint minim.",
            "picture": "static/app/img/testimonials/testimonials-3.jpg"
        },
        {
            "name": "Matt Brandon",
            "job": "Freelancer",
            "testimonial": "Fugiat enim eram quae cillum dolore dolor amet nulla culpa multos export minim fugiat minim velit minim dolor enim duis veniam ipsum anim magna sunt elit fore quem dolore labore illum veniam.",
            "picture": "static/app/img/testimonials/testimonials-4.jpg"
        },
        {
            "name": "John Larson",
            "job": "Entrepreneur",
            "testimonial": "Quis quorum aliqua sint quem legam fore sunt eram irure aliqua veniam tempor noster veniam enim culpa labore duis sunt culpa nulla illum cillum fugiat legam esse veniam culpa fore nisi cillum quid.",
            "picture": "static/app/img/testimonials/testimonials-5.jpg"
        },
    ]


    for i in datasTestimonials:
        seeder.add_entity(TestimonialsModel, 1, i)

    seeder.execute()
    print("Datas _about OK !")