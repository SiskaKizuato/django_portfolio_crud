# Generated by Django 4.2.1 on 2023-06-11 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_contactmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestimonialsModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('job', models.CharField(max_length=30)),
                ('testimonial', models.TextField()),
                ('picture', models.CharField(max_length=700)),
            ],
        ),
    ]
