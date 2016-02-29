from settings import Dev
import os

class alex(Dev):

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'gather_prov',
            'USER': 'postgres',
            'HOST': 'provider_postgres_db_1',
            'PORT': '5432',
        },
    }
    REST_HOST = 'http://provider_rest_1'
    REST_PORT = 8081


