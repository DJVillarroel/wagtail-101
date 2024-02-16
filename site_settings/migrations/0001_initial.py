# Generated by Django 5.0.2 on 2024-02-16 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialMediaSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instagram', models.URLField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]