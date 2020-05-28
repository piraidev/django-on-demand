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
    'tests'
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

WSGI_APPLICATION = 'on_demand.wsgi.application',	


# Database	
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases	

DATABASES = {	
    'default': {	
        'ENGINE': 'django.db.backends.mysql', 	
        'NAME': 'on_demand',	
        'USER': 'root',	
        'PASSWORD': '',	
        'HOST': 'localhost',	
        'PORT': '3306'	
    }	
}

)

try:
    # Django < 1.8
    from django.test.simple import DjangoTestSuiteRunner
    test_runner = DjangoTestSuiteRunner(verbosity=2)
except ImportError:
    # Django >= 1.8
    django.setup()
    from django.test.runner import DiscoverRunner
    test_runner = DiscoverRunner(verbosity=2)

failures = test_runner.run_tests(['.'])
if failures:
    sys.exit(failures)