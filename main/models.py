from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from yaus.settings import ALLOWED_HOSTS

from main.numeral_systems_converter import convert_10_to_62, convert_62_to_10


class URL(models.Model):
    full = models.URLField()
    short = models.SlugField(blank=True, unique=True)

    def get_short(self):
        '''Returns short URL'''
        host = ALLOWED_HOSTS[0]
        return f'http://{host}/{self.short}'


@receiver(post_save, sender=URL)
def generate_short_url(sender, instance, created, **kwargs):
    '''If no short URL was given by a user, generate one'''
    if created and not instance.short:
        instance.short = convert_10_to_62(number_10_radix=instance.id)
        instance.save()
