import os
from decouple import config, Csv
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        username = config['SUPER_USER_NAME']
        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(username,
                                          config['SUPER_USER_EMAIL'],
                                          config['SUPER_USER_PASSWORD'])