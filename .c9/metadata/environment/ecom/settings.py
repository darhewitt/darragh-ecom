{"changed":true,"filter":false,"title":"settings.py","tooltip":"/ecom/settings.py","value":"\"\"\"\nDjango settings for ecom project.\n\nGenerated by 'django-admin startproject' using Django 1.11.24.\n\nFor more information on this file, see\nhttps://docs.djangoproject.com/en/1.11/topics/settings/\n\nFor the full list of settings and their values, see\nhttps://docs.djangoproject.com/en/1.11/ref/settings/\n\"\"\"\n\nimport os\nimport env\nimport dj_database_url\n\n# Build paths inside the project like this: os.path.join(BASE_DIR, ...)\nBASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))\n\n\n# Quick-start development settings - unsuitable for production\n# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/\n\n# SECURITY WARNING: keep the secret key used in production secret!\nSECRET_KEY = os.environ.get(\"SECRET_KEY\")\n\n# SECURITY WARNING: don't run with debug turned on in production!\nDEBUG = True\n\nALLOWED_HOSTS = ['2d2e534e277841238d362fdd4be915e5.vfs.cloud9.us-east-1.amazonaws.com', 'ci-ecom.herokuapp.com']\n\n\n# Application definition\n\nINSTALLED_APPS = [\n    'django.contrib.admin',\n    'django.contrib.auth',\n    'django.contrib.contenttypes',\n    'django.contrib.sessions',\n    'django.contrib.messages',\n    'django.contrib.staticfiles',\n    'django_forms_bootstrap',\n    'accounts',\n    'products',\n    'cart',\n    'checkout',\n    'storages'\n]\n\nMIDDLEWARE = [\n    'django.middleware.security.SecurityMiddleware',\n    'django.contrib.sessions.middleware.SessionMiddleware',\n    'django.middleware.common.CommonMiddleware',\n    'django.middleware.csrf.CsrfViewMiddleware',\n    'django.contrib.auth.middleware.AuthenticationMiddleware',\n    'django.contrib.messages.middleware.MessageMiddleware',\n    'django.middleware.clickjacking.XFrameOptionsMiddleware',\n]\n\nROOT_URLCONF = 'ecom.urls'\n\nTEMPLATES = [\n    {\n        'BACKEND': 'django.template.backends.django.DjangoTemplates',\n        'DIRS': [os.path.join(BASE_DIR, 'templates')],\n        'APP_DIRS': True,\n        'OPTIONS': {\n            'context_processors': [\n                'django.template.context_processors.debug',\n                'django.template.context_processors.request',\n                'django.contrib.auth.context_processors.auth',\n                'django.contrib.messages.context_processors.messages',\n                'django.template.context_processors.media',\n                'cart.contexts.cart_contents'\n            ],\n        },\n    },\n]\n\nWSGI_APPLICATION = 'ecom.wsgi.application'\n\n\n# Database\n# https://docs.djangoproject.com/en/1.11/ref/settings/#databases\n\nif \"DATABASE_URL\" in os.environ:\n    DATABASES = {'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))}\nelse:\n    print(\"Database URL not found. Using SQLite instead\")\n    DATABASES = {\n        'default': {\n            'ENGINE': 'django.db.backends.sqlite3',\n            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),\n        }\n    }\n    \n# Password validation\n# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators\n\nAUTH_PASSWORD_VALIDATORS = [\n    {\n        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',\n    },\n    {\n        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',\n    },\n]\n\nAUTHENTICATION_BACKENDS = [\n    'django.contrib.auth.backends.ModelBackend',\n    'accounts.backends.caseInsensitiveAuth']\n\n# Internationalization\n# https://docs.djangoproject.com/en/1.11/topics/i18n/\n\nLANGUAGE_CODE = 'en-us'\n\nTIME_ZONE = 'UTC'\n\nUSE_I18N = True\n\nUSE_L10N = True\n\nUSE_TZ = True\n\n\n# Static files (CSS, JavaScript, Images)\n# https://docs.djangoproject.com/en/1.11/howto/static-files/\n\nAWS_S3_OBJECT_PARAMETERS = {\n    'Expires': 'Thu, 31 Dec 2099 20:00:00 GMT',\n    'CacheControl': 'max-age=94608000',\n}\n\nAWS_STORAGE_BUCKET_NAME = 'darraghs-ecom'\nAWS_S3_REGION_NAME = 'eu-west-1'\nAWS_ACCESS_KEY_ID = os.environ.get(\"AWS_SECRET_KEY_ID\")\nAWS_SECRET_ACCESS_KEY = os.environ.get(\"AWS_SECRET_ACCESS_KEY\")\n\nAWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME\n\nSTATICFILES_LOCATION = 'static'\nSTATICFILES_STORAGE = 'custom_storages.StaticStorage'\n\n\nSTATIC_URL = '/static/'\nSTATICFILES_DIRS = (\n   os.path.join(BASE_DIR, \"static\"),\n  )\n    \nMEDIAFILES_LOCATION = 'media'\nDEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'\n\nMEDIA_ROOT = os.path.join(BASE_DIR, 'media')\nMEDIA_URL = \"https://%s/%s/\" % (AWS_S3_CUSTOM_DOMAIN, MEDIAFILES_LOCATION)\n\nSTRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE')\nSTRIPE_SECRET = os.getenv('STRIPE_SECRET')\n\nMESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'\n","undoManager":{"mark":97,"position":100,"stack":[[{"start":{"row":152,"column":0},"end":{"row":152,"column":1},"action":"insert","lines":["#"],"id":487}],[{"start":{"row":153,"column":1},"end":{"row":153,"column":2},"action":"insert","lines":["#"],"id":488}],[{"start":{"row":154,"column":2},"end":{"row":154,"column":3},"action":"insert","lines":["#"],"id":489}],[{"start":{"row":154,"column":1},"end":{"row":154,"column":2},"action":"remove","lines":[" "],"id":490},{"start":{"row":154,"column":0},"end":{"row":154,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":153,"column":0},"end":{"row":153,"column":1},"action":"remove","lines":[" "],"id":491}],[{"start":{"row":154,"column":0},"end":{"row":154,"column":1},"action":"remove","lines":["#"],"id":492}],[{"start":{"row":153,"column":0},"end":{"row":153,"column":1},"action":"remove","lines":["#"],"id":493}],[{"start":{"row":152,"column":0},"end":{"row":152,"column":1},"action":"remove","lines":["#"],"id":494}],[{"start":{"row":151,"column":0},"end":{"row":151,"column":1},"action":"remove","lines":["#"],"id":495}],[{"start":{"row":148,"column":0},"end":{"row":148,"column":1},"action":"remove","lines":["#"],"id":496}],[{"start":{"row":147,"column":0},"end":{"row":147,"column":1},"action":"remove","lines":["#"],"id":497}],[{"start":{"row":140,"column":0},"end":{"row":140,"column":1},"action":"insert","lines":["#"],"id":498}],[{"start":{"row":141,"column":0},"end":{"row":141,"column":1},"action":"insert","lines":["#"],"id":499}],[{"start":{"row":142,"column":0},"end":{"row":142,"column":1},"action":"insert","lines":["#"],"id":500}],[{"start":{"row":143,"column":0},"end":{"row":143,"column":1},"action":"insert","lines":["#"],"id":501}],[{"start":{"row":145,"column":0},"end":{"row":145,"column":1},"action":"insert","lines":["#"],"id":502}],[{"start":{"row":147,"column":0},"end":{"row":147,"column":1},"action":"insert","lines":["#"],"id":503}],[{"start":{"row":148,"column":0},"end":{"row":148,"column":1},"action":"insert","lines":["#"],"id":504}],[{"start":{"row":135,"column":0},"end":{"row":135,"column":1},"action":"insert","lines":["#"],"id":505}],[{"start":{"row":136,"column":0},"end":{"row":136,"column":1},"action":"insert","lines":["#"],"id":506}],[{"start":{"row":137,"column":0},"end":{"row":137,"column":1},"action":"insert","lines":["#"],"id":507}],[{"start":{"row":138,"column":0},"end":{"row":138,"column":1},"action":"insert","lines":["#"],"id":508}],[{"start":{"row":148,"column":0},"end":{"row":148,"column":1},"action":"remove","lines":["#"],"id":509}],[{"start":{"row":147,"column":0},"end":{"row":147,"column":1},"action":"remove","lines":["#"],"id":510}],[{"start":{"row":145,"column":0},"end":{"row":145,"column":1},"action":"remove","lines":["#"],"id":511}],[{"start":{"row":143,"column":0},"end":{"row":143,"column":1},"action":"remove","lines":["#"],"id":512}],[{"start":{"row":142,"column":0},"end":{"row":142,"column":1},"action":"remove","lines":["#"],"id":513}],[{"start":{"row":141,"column":0},"end":{"row":141,"column":1},"action":"remove","lines":["#"],"id":514}],[{"start":{"row":140,"column":0},"end":{"row":140,"column":1},"action":"remove","lines":["#"],"id":515}],[{"start":{"row":138,"column":0},"end":{"row":138,"column":1},"action":"remove","lines":["#"],"id":516}],[{"start":{"row":137,"column":0},"end":{"row":137,"column":1},"action":"remove","lines":["#"],"id":517}],[{"start":{"row":136,"column":0},"end":{"row":136,"column":1},"action":"remove","lines":["#"],"id":518}],[{"start":{"row":135,"column":0},"end":{"row":135,"column":1},"action":"remove","lines":["#"],"id":535}],[{"start":{"row":148,"column":23},"end":{"row":148,"column":51},"action":"remove","lines":["custom_storages.StaticStorag"],"id":536}],[{"start":{"row":148,"column":23},"end":{"row":148,"column":24},"action":"remove","lines":["e"],"id":537}],[{"start":{"row":148,"column":23},"end":{"row":148,"column":24},"action":"insert","lines":["s"],"id":538},{"start":{"row":148,"column":24},"end":{"row":148,"column":25},"action":"insert","lines":["t"]},{"start":{"row":148,"column":25},"end":{"row":148,"column":26},"action":"insert","lines":["o"]},{"start":{"row":148,"column":26},"end":{"row":148,"column":27},"action":"insert","lines":["r"]}],[{"start":{"row":148,"column":27},"end":{"row":148,"column":28},"action":"insert","lines":["a"],"id":539},{"start":{"row":148,"column":28},"end":{"row":148,"column":29},"action":"insert","lines":["g"]},{"start":{"row":148,"column":29},"end":{"row":148,"column":30},"action":"insert","lines":["e"]},{"start":{"row":148,"column":30},"end":{"row":148,"column":31},"action":"insert","lines":["s"]}],[{"start":{"row":148,"column":31},"end":{"row":148,"column":32},"action":"insert","lines":["."],"id":540},{"start":{"row":148,"column":32},"end":{"row":148,"column":33},"action":"insert","lines":["b"]},{"start":{"row":148,"column":33},"end":{"row":148,"column":34},"action":"insert","lines":["a"]},{"start":{"row":148,"column":34},"end":{"row":148,"column":35},"action":"insert","lines":["c"]},{"start":{"row":148,"column":35},"end":{"row":148,"column":36},"action":"insert","lines":["k"]},{"start":{"row":148,"column":36},"end":{"row":148,"column":37},"action":"insert","lines":["e"]},{"start":{"row":148,"column":37},"end":{"row":148,"column":38},"action":"insert","lines":["n"]},{"start":{"row":148,"column":38},"end":{"row":148,"column":39},"action":"insert","lines":["d"]}],[{"start":{"row":148,"column":39},"end":{"row":148,"column":40},"action":"insert","lines":["s"],"id":541}],[{"start":{"row":148,"column":40},"end":{"row":148,"column":41},"action":"insert","lines":["."],"id":542},{"start":{"row":148,"column":41},"end":{"row":148,"column":42},"action":"insert","lines":["s"]},{"start":{"row":148,"column":42},"end":{"row":148,"column":43},"action":"insert","lines":["3"]},{"start":{"row":148,"column":43},"end":{"row":148,"column":44},"action":"insert","lines":["b"]},{"start":{"row":148,"column":44},"end":{"row":148,"column":45},"action":"insert","lines":["o"]},{"start":{"row":148,"column":45},"end":{"row":148,"column":46},"action":"insert","lines":["t"]}],[{"start":{"row":148,"column":46},"end":{"row":148,"column":47},"action":"insert","lines":["o"],"id":543}],[{"start":{"row":148,"column":47},"end":{"row":148,"column":48},"action":"insert","lines":["3"],"id":544}],[{"start":{"row":148,"column":48},"end":{"row":148,"column":49},"action":"insert","lines":["."],"id":545},{"start":{"row":148,"column":49},"end":{"row":148,"column":50},"action":"insert","lines":["S"]},{"start":{"row":148,"column":50},"end":{"row":148,"column":51},"action":"insert","lines":["3"]}],[{"start":{"row":148,"column":51},"end":{"row":148,"column":52},"action":"insert","lines":["B"],"id":546},{"start":{"row":148,"column":52},"end":{"row":148,"column":53},"action":"insert","lines":["o"]},{"start":{"row":148,"column":53},"end":{"row":148,"column":54},"action":"insert","lines":["t"]},{"start":{"row":148,"column":54},"end":{"row":148,"column":55},"action":"insert","lines":["o"]},{"start":{"row":148,"column":55},"end":{"row":148,"column":56},"action":"insert","lines":["S"]}],[{"start":{"row":148,"column":56},"end":{"row":148,"column":57},"action":"insert","lines":["t"],"id":547},{"start":{"row":148,"column":57},"end":{"row":148,"column":58},"action":"insert","lines":["o"]},{"start":{"row":148,"column":58},"end":{"row":148,"column":59},"action":"insert","lines":["r"]},{"start":{"row":148,"column":59},"end":{"row":148,"column":60},"action":"insert","lines":["a"]}],[{"start":{"row":148,"column":60},"end":{"row":148,"column":61},"action":"insert","lines":["g"],"id":548},{"start":{"row":148,"column":61},"end":{"row":148,"column":62},"action":"insert","lines":["e"]}],[{"start":{"row":147,"column":0},"end":{"row":147,"column":1},"action":"insert","lines":["#"],"id":549}],[{"start":{"row":148,"column":55},"end":{"row":148,"column":56},"action":"insert","lines":["3"],"id":550}],[{"start":{"row":165,"column":74},"end":{"row":165,"column":75},"action":"insert","lines":["r"],"id":551},{"start":{"row":165,"column":75},"end":{"row":165,"column":76},"action":"insert","lines":["u"]},{"start":{"row":165,"column":76},"end":{"row":165,"column":77},"action":"insert","lines":["n"]}],[{"start":{"row":165,"column":77},"end":{"row":166,"column":0},"action":"insert","lines":["",""],"id":552}],[{"start":{"row":165,"column":76},"end":{"row":165,"column":77},"action":"remove","lines":["n"],"id":553},{"start":{"row":165,"column":75},"end":{"row":165,"column":76},"action":"remove","lines":["u"]},{"start":{"row":165,"column":74},"end":{"row":165,"column":75},"action":"remove","lines":["r"]}],[{"start":{"row":147,"column":0},"end":{"row":147,"column":1},"action":"remove","lines":["#"],"id":554}],[{"start":{"row":148,"column":62},"end":{"row":148,"column":63},"action":"remove","lines":["e"],"id":555},{"start":{"row":148,"column":61},"end":{"row":148,"column":62},"action":"remove","lines":["g"]},{"start":{"row":148,"column":60},"end":{"row":148,"column":61},"action":"remove","lines":["a"]},{"start":{"row":148,"column":59},"end":{"row":148,"column":60},"action":"remove","lines":["r"]},{"start":{"row":148,"column":58},"end":{"row":148,"column":59},"action":"remove","lines":["o"]},{"start":{"row":148,"column":57},"end":{"row":148,"column":58},"action":"remove","lines":["t"]},{"start":{"row":148,"column":56},"end":{"row":148,"column":57},"action":"remove","lines":["S"]},{"start":{"row":148,"column":55},"end":{"row":148,"column":56},"action":"remove","lines":["3"]},{"start":{"row":148,"column":54},"end":{"row":148,"column":55},"action":"remove","lines":["o"]},{"start":{"row":148,"column":53},"end":{"row":148,"column":54},"action":"remove","lines":["t"]},{"start":{"row":148,"column":52},"end":{"row":148,"column":53},"action":"remove","lines":["o"]},{"start":{"row":148,"column":51},"end":{"row":148,"column":52},"action":"remove","lines":["B"]},{"start":{"row":148,"column":50},"end":{"row":148,"column":51},"action":"remove","lines":["3"]},{"start":{"row":148,"column":49},"end":{"row":148,"column":50},"action":"remove","lines":["S"]},{"start":{"row":148,"column":48},"end":{"row":148,"column":49},"action":"remove","lines":["."]},{"start":{"row":148,"column":47},"end":{"row":148,"column":48},"action":"remove","lines":["3"]},{"start":{"row":148,"column":46},"end":{"row":148,"column":47},"action":"remove","lines":["o"]},{"start":{"row":148,"column":45},"end":{"row":148,"column":46},"action":"remove","lines":["t"]},{"start":{"row":148,"column":44},"end":{"row":148,"column":45},"action":"remove","lines":["o"]},{"start":{"row":148,"column":43},"end":{"row":148,"column":44},"action":"remove","lines":["b"]}],[{"start":{"row":148,"column":42},"end":{"row":148,"column":43},"action":"remove","lines":["3"],"id":556},{"start":{"row":148,"column":41},"end":{"row":148,"column":42},"action":"remove","lines":["s"]},{"start":{"row":148,"column":40},"end":{"row":148,"column":41},"action":"remove","lines":["."]},{"start":{"row":148,"column":39},"end":{"row":148,"column":40},"action":"remove","lines":["s"]},{"start":{"row":148,"column":38},"end":{"row":148,"column":39},"action":"remove","lines":["d"]},{"start":{"row":148,"column":37},"end":{"row":148,"column":38},"action":"remove","lines":["n"]},{"start":{"row":148,"column":36},"end":{"row":148,"column":37},"action":"remove","lines":["e"]},{"start":{"row":148,"column":35},"end":{"row":148,"column":36},"action":"remove","lines":["k"]},{"start":{"row":148,"column":34},"end":{"row":148,"column":35},"action":"remove","lines":["c"]},{"start":{"row":148,"column":33},"end":{"row":148,"column":34},"action":"remove","lines":["a"]},{"start":{"row":148,"column":32},"end":{"row":148,"column":33},"action":"remove","lines":["b"]},{"start":{"row":148,"column":31},"end":{"row":148,"column":32},"action":"remove","lines":["."]},{"start":{"row":148,"column":30},"end":{"row":148,"column":31},"action":"remove","lines":["s"]},{"start":{"row":148,"column":29},"end":{"row":148,"column":30},"action":"remove","lines":["e"]},{"start":{"row":148,"column":28},"end":{"row":148,"column":29},"action":"remove","lines":["g"]},{"start":{"row":148,"column":27},"end":{"row":148,"column":28},"action":"remove","lines":["a"]},{"start":{"row":148,"column":26},"end":{"row":148,"column":27},"action":"remove","lines":["r"]},{"start":{"row":148,"column":25},"end":{"row":148,"column":26},"action":"remove","lines":["o"]},{"start":{"row":148,"column":24},"end":{"row":148,"column":25},"action":"remove","lines":["t"]}],[{"start":{"row":148,"column":23},"end":{"row":148,"column":24},"action":"remove","lines":["s"],"id":557}],[{"start":{"row":148,"column":23},"end":{"row":148,"column":24},"action":"insert","lines":["c"],"id":558},{"start":{"row":148,"column":24},"end":{"row":148,"column":25},"action":"insert","lines":["u"]},{"start":{"row":148,"column":25},"end":{"row":148,"column":26},"action":"insert","lines":["s"]}],[{"start":{"row":148,"column":26},"end":{"row":148,"column":27},"action":"insert","lines":["t"],"id":559},{"start":{"row":148,"column":27},"end":{"row":148,"column":28},"action":"insert","lines":["o"]},{"start":{"row":148,"column":28},"end":{"row":148,"column":29},"action":"insert","lines":["m"]}],[{"start":{"row":148,"column":23},"end":{"row":148,"column":29},"action":"remove","lines":["custom"],"id":560},{"start":{"row":148,"column":23},"end":{"row":148,"column":38},"action":"insert","lines":["custom_storages"]}],[{"start":{"row":148,"column":38},"end":{"row":148,"column":39},"action":"insert","lines":["."],"id":561},{"start":{"row":148,"column":39},"end":{"row":148,"column":40},"action":"insert","lines":["S"]},{"start":{"row":148,"column":40},"end":{"row":148,"column":41},"action":"insert","lines":["t"]}],[{"start":{"row":148,"column":41},"end":{"row":148,"column":42},"action":"insert","lines":["a"],"id":562}],[{"start":{"row":148,"column":39},"end":{"row":148,"column":42},"action":"remove","lines":["Sta"],"id":563},{"start":{"row":148,"column":39},"end":{"row":148,"column":45},"action":"insert","lines":["Static"]}],[{"start":{"row":148,"column":45},"end":{"row":148,"column":46},"action":"insert","lines":["S"],"id":564},{"start":{"row":148,"column":46},"end":{"row":148,"column":47},"action":"insert","lines":["t"]},{"start":{"row":148,"column":47},"end":{"row":148,"column":48},"action":"insert","lines":["o"]},{"start":{"row":148,"column":48},"end":{"row":148,"column":49},"action":"insert","lines":["r"]},{"start":{"row":148,"column":49},"end":{"row":148,"column":50},"action":"insert","lines":["a"]},{"start":{"row":148,"column":50},"end":{"row":148,"column":51},"action":"insert","lines":["g"]}],[{"start":{"row":148,"column":51},"end":{"row":148,"column":52},"action":"insert","lines":["e"],"id":565}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"insert","lines":["#"],"id":566}],[{"start":{"row":85,"column":0},"end":{"row":85,"column":1},"action":"remove","lines":["#"],"id":567}],[{"start":{"row":87,"column":0},"end":{"row":87,"column":1},"action":"remove","lines":["#"],"id":568}],[{"start":{"row":88,"column":0},"end":{"row":88,"column":1},"action":"remove","lines":["#"],"id":569}],[{"start":{"row":89,"column":0},"end":{"row":89,"column":1},"action":"remove","lines":["#"],"id":570}],[{"start":{"row":90,"column":0},"end":{"row":90,"column":1},"action":"remove","lines":["#"],"id":571}],[{"start":{"row":91,"column":0},"end":{"row":91,"column":1},"action":"remove","lines":["#"],"id":572}],[{"start":{"row":92,"column":0},"end":{"row":92,"column":1},"action":"remove","lines":["#"],"id":573}],[{"start":{"row":93,"column":0},"end":{"row":93,"column":1},"action":"remove","lines":["#"],"id":574}],[{"start":{"row":94,"column":0},"end":{"row":94,"column":1},"action":"remove","lines":["#"],"id":575}],[{"start":{"row":86,"column":0},"end":{"row":86,"column":4},"action":"insert","lines":["    "],"id":576}],[{"start":{"row":145,"column":68},"end":{"row":145,"column":72},"action":"insert","lines":["    "],"id":577}],[{"start":{"row":145,"column":68},"end":{"row":145,"column":72},"action":"remove","lines":["    "],"id":578}],[{"start":{"row":13,"column":0},"end":{"row":13,"column":1},"action":"remove","lines":["#"],"id":579}],[{"start":{"row":85,"column":0},"end":{"row":85,"column":1},"action":"insert","lines":["#"],"id":580}],[{"start":{"row":87,"column":0},"end":{"row":87,"column":1},"action":"insert","lines":["#"],"id":581}],[{"start":{"row":86,"column":2},"end":{"row":86,"column":3},"action":"remove","lines":[" "],"id":582},{"start":{"row":86,"column":1},"end":{"row":86,"column":2},"action":"remove","lines":[" "]},{"start":{"row":86,"column":0},"end":{"row":86,"column":1},"action":"remove","lines":[" "]}],[{"start":{"row":86,"column":0},"end":{"row":86,"column":1},"action":"remove","lines":[" "],"id":583}],[{"start":{"row":88,"column":0},"end":{"row":88,"column":1},"action":"insert","lines":["#"],"id":584}],[{"start":{"row":89,"column":0},"end":{"row":89,"column":1},"action":"insert","lines":["#"],"id":585}],[{"start":{"row":90,"column":0},"end":{"row":90,"column":1},"action":"insert","lines":["#"],"id":586}],[{"start":{"row":91,"column":0},"end":{"row":91,"column":1},"action":"insert","lines":["#"],"id":587}],[{"start":{"row":92,"column":0},"end":{"row":92,"column":1},"action":"insert","lines":["#"],"id":588}],[{"start":{"row":93,"column":0},"end":{"row":93,"column":1},"action":"insert","lines":["#"],"id":589}],[{"start":{"row":94,"column":0},"end":{"row":94,"column":1},"action":"insert","lines":["#"],"id":590}],[{"start":{"row":94,"column":0},"end":{"row":94,"column":1},"action":"remove","lines":["#"],"id":591}],[{"start":{"row":93,"column":0},"end":{"row":93,"column":1},"action":"remove","lines":["#"],"id":592}],[{"start":{"row":92,"column":0},"end":{"row":92,"column":1},"action":"remove","lines":["#"],"id":593}],[{"start":{"row":91,"column":0},"end":{"row":91,"column":1},"action":"remove","lines":["#"],"id":594}],[{"start":{"row":90,"column":0},"end":{"row":90,"column":1},"action":"remove","lines":["#"],"id":595}],[{"start":{"row":89,"column":0},"end":{"row":89,"column":1},"action":"remove","lines":["#"],"id":596}],[{"start":{"row":88,"column":0},"end":{"row":88,"column":1},"action":"remove","lines":["#"],"id":597}],[{"start":{"row":87,"column":0},"end":{"row":87,"column":1},"action":"remove","lines":["#"],"id":598}],[{"start":{"row":85,"column":0},"end":{"row":85,"column":1},"action":"remove","lines":["#"],"id":599}],[{"start":{"row":86,"column":0},"end":{"row":86,"column":4},"action":"insert","lines":["    "],"id":600}],[{"start":{"row":91,"column":37},"end":{"row":91,"column":38},"action":"insert","lines":["g"],"id":601},{"start":{"row":91,"column":38},"end":{"row":91,"column":39},"action":"insert","lines":["i"]},{"start":{"row":91,"column":39},"end":{"row":91,"column":40},"action":"insert","lines":["t"]}],[{"start":{"row":91,"column":40},"end":{"row":91,"column":41},"action":"insert","lines":[" "],"id":602},{"start":{"row":91,"column":41},"end":{"row":91,"column":42},"action":"insert","lines":["a"]}],[{"start":{"row":91,"column":41},"end":{"row":91,"column":42},"action":"remove","lines":["a"],"id":603},{"start":{"row":91,"column":40},"end":{"row":91,"column":41},"action":"remove","lines":[" "]},{"start":{"row":91,"column":39},"end":{"row":91,"column":40},"action":"remove","lines":["t"]},{"start":{"row":91,"column":38},"end":{"row":91,"column":39},"action":"remove","lines":["i"]},{"start":{"row":91,"column":37},"end":{"row":91,"column":38},"action":"remove","lines":["g"]}]]},"ace":{"folds":[],"scrolltop":1302.0000000000023,"scrollleft":0,"selection":{"start":{"row":91,"column":37},"end":{"row":91,"column":37},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":80,"state":"start","mode":"ace/mode/python"}},"timestamp":1579812573403}