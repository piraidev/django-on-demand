import django, sys
from django.conf import settings

settings.configure(
SILENCED_SYSTEM_CHECKS = ['mysql.E001'],

# Application definition	

INSTALLED_APPS = [	
    'django.contrib.admin',	
    'django.contrib.auth',	
    'django.contrib.contenttypes',	
    'django.contrib.sessions',	
    'django.contrib.messages',	
    'django.contrib.staticfiles',	
    'rest_framework',	
    'rest_framework.authtoken',	
    'on_demand',
],	

MIDDLEWARE = [	
    'django.middleware.security.SecurityMiddleware',	
    'django.contrib.sessions.middleware.SessionMiddleware',	
    'django.middleware.common.CommonMiddleware',	
    'django.middleware.csrf.CsrfViewMiddleware',	
    'django.contrib.auth.middleware.AuthenticationMiddleware',	
    'django.contrib.messages.middleware.MessageMiddleware',	
    'django.middleware.clickjacking.XFrameOptionsMiddleware'	
],

ROOT_URLCONF = 'on_demand.urls',

TEMPLATES = [	
    {	
        'BACKEND': 'django.template.backends.django.DjangoTemplates',	
        'DIRS': [],	
        'APP_DIRS': True,	
        'OPTIONS': {	
            'context_processors': [	
                'django.template.context_processors.debug',	
                'django.template.context_processors.request',	
                'django.contrib.auth.context_processors.auth',	
                'django.contrib.messages.context_processors.messages',	
            ],	
        },	
    },	
],

DATABASES = {	
    'default': {	
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'on_demand',	
        'USER': 'root',	
        'PASSWORD': '',	
        'HOST': 'localhost',	
        'PORT': '3306'
    }	
}

)

django.setup()
from django.test.runner import DiscoverRunner
test_runner = DiscoverRunner(verbosity=2)

failures = test_runner.run_tests(['.'])
if failures:
    sys.exit(failures)