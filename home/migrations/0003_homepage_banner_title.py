# Generated by Django 5.0.2 on 2024-02-16 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='banner_title',
            field=models.CharField(default='Bienvenido a mi página', max_length=100),
        ),
    ]