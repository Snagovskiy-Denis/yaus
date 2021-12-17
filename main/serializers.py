from rest_framework import serializers

from main.models import URL


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ('full', 'short')
