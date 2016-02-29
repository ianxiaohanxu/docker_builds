import json
from time import time
import os
import uuid
from django.conf import settings
from django.core.management import call_command
from django.core.management.base import NoArgsCommand, CommandError
from django.utils import timezone

from shaman_dm.libs.tests import mixer

from shaman_dm.apps.slave import defs
from shaman_dm.apps.rest import defs as rest_defs
from shaman_dm.apps.rest import models

from provider.oauth2.models import Client
from shaman_dm.apps.rest.models import ShamanUser
from shaman_dm.apps.rest.db import set_thread_db

class Command(NoArgsCommand):

    help = ''

    def handle_noargs(self, **options):

        # Create a superuser
        email_address = 'admin%s@test.com' %(str(int(time())))
        set_thread_db('default')
        su = ShamanUser.objects.create_superuser(
                    email=email_address,
                    first_name='Daniel',
                    last_name='Dai',
                    password='000000',
        )
        su.set_password('000000')
        set_thread_db('demo')
        su = ShamanUser.objects.create_superuser(
                    email=email_address,
                    first_name='Daniel',
                    last_name='Dai',
                    password='000000',
        )
        su.set_password('000000')
        set_thread_db('default')
        user = ShamanUser.objects.get(email=email_address)
        Client.objects.create(user=user,
                              name='1',
                              url='http://localhost:8000/provider',
                              redirect_uri='http://localhost:8000/provider',
                              client_id='125b7208b964b23d59e2',
                              client_secret='956cbdf1bff2b60105ebf9070a77efec178fa93d',
                              client_type=0)
        set_thread_db('demo')
        user = ShamanUser.objects.get(email=email_address)
        Client.objects.create(user=user,
                              name='1',
                              url='http://localhost:8000/provider',
                              redirect_uri='http://localhost:8000/provider',
                              client_id='125b7208b964b23d59e2',
                              client_secret='956cbdf1bff2b60105ebf9070a77efec178fa93d',
                              client_type=0)

