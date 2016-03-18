from settings import Dev
import os

class alex(Dev):

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'gather_prov',
            'USER': 'postgres',
            'HOST': 'db',
            'PORT': '5432',
        },
    }
    REST_HOST = 'http://rest'
    REST_PORT = 8081


