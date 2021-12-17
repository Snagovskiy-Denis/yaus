from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from main.numeral_systems_converter import convert_10_to_64, convert_64_to_10


class URL(models.Model):
    full = models.URLField()
    short = models.SlugField(blank=True, unique=True)


@receiver(post_save, sender=URL)
def generate_short_url(sender, instance, created, **kwargs):
    '''If no short URL was given by a user, generate one'''
    if created and not instance.short:
        instance.short = convert_10_to_64(num10=instance.id)
        instance.save()
