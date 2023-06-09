# Generated by Django 4.2.1 on 2023-06-09 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_heromodel_nom_alter_heromodel_prenom'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.CharField(max_length=700)),
                ('intro', models.TextField()),
                ('job', models.CharField(max_length=100)),
                ('birthday', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=60)),
                ('age', models.PositiveIntegerField()),
                ('degree', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('freelance', models.CharField(max_length=20)),
                ('description', models.TextField()),
            ],
        ),
    ]