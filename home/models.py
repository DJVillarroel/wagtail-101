from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel

class HomePage(Page):
    banner_title = models.CharField(max_length=100, default="Bienvenido a mi página")
    
    banner_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        related_name='+',
    )
    
    content_panels = Page.content_panels + [
        FieldPanel('banner_title'),
        FieldPanel('banner_image')
    ]
