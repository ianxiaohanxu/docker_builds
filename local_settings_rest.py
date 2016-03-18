from settings import Slave
import os

class Slave_alex(Slave):

    @property
    def INSTALLED_APPS(self):
            return super(Slave_alex, self).INSTALLED_APPS + ('dev_reset',)

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'gather_rest',
            'USER': 'postgres',
            'HOST': 'db',
            'PORT': '5432',
        },
        'demo': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'gather_demo',
            'USER': 'postgres',
            'HOST': 'db',
            'PORT': '5432',
        },
    }
    EMAIL_SUBJECT_PREFIX = '[Gather-Daniel] '
    SERVER_EMAIL         = 'gather@danidai.com'
    #EMAIL_INFO = 'gather@danidai.com'
    EMAIL_FROM = 'gather@danidai.com'
    #EMAIL_TO = 'gather@danidai.com'
    EMAIL_HOST = 'smtp.ym.163.com'
    EMAIL_PORT = 25
    EMAIL_HOST_USER = 'gather@danidai.com'
    EMAIL_HOST_PASSWORD = '000000'
    #EMAIL_USE_TLS = True   
