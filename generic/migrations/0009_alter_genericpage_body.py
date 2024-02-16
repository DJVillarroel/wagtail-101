# Generated by Django 5.0.2 on 2024-02-16 18:57

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0008_auto_20240216_0453'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericpage',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(template='heading_block.html')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('paragraph', wagtail.blocks.RichTextBlock())], null=True),
        ),
    ]
