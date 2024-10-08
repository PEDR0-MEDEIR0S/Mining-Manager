"""
settings.py
Django settings for project project.

Generated by 'django-admin startproject' using Django 5.1.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/

Este arquivo contém as configurações principais para o projeto Django. Ele define as configurações de segurança, banco de dados, aplicativos instalados, middlewares e outras opções essenciais para o funcionamento da aplicação. A estrutura do arquivo segue os padrões recomendados pelo Django, permitindo fácil modificação e entendimento por parte dos desenvolvedores.

### Importância
A importância do `settings.py` é garantir que a aplicação Django esteja corretamente configurada para operar em diferentes ambientes (desenvolvimento, testes e produção). Configurações como chave secreta, permissões de hosts, configuração do banco de dados e gerenciamento de arquivos estáticos são essenciais para a segurança e funcionalidade do sistema. A estrutura modular do arquivo permite que as configurações sejam facilmente alteradas conforme as necessidades do projeto.

### Principais Seções e Configurações
Entre as principais seções implementadas neste arquivo, destacam-se:

1. **BASE_DIR**: Define o diretório base do projeto, utilizado para construir caminhos relativos.

2. **SECRET_KEY**: Chave secreta usada para fornecer criptografia em diversas partes do Django. Deve ser mantida em segredo em produção.

3. **DEBUG**: Ativa ou desativa o modo de depuração. Não deve ser ativado em produção.

4. **ALLOWED_HOSTS**: Lista de strings representando os hosts/domínios permitidos para a aplicação. Deve ser configurada em produção.

5. **INSTALLED_APPS**: Lista de aplicativos Django e personalizados que estão habilitados na aplicação. Inclui componentes do Django e o aplicativo `dashboard`.

6. **MIDDLEWARE**: Lista de middlewares que processam as requisições e respostas. Cada middleware tem uma função específica, como segurança e gerenciamento de sessões.

7. **ROOT_URLCONF**: Especifica o módulo que contém as configurações de URL do projeto.

8. **TEMPLATES**: Configurações relacionadas à renderização de templates, incluindo diretórios de templates e processadores de contexto.

9. **WSGI_APPLICATION**: Define o ponto de entrada WSGI da aplicação.

10. **DATABASES**: Configurações do banco de dados, incluindo engine, nome, usuário, senha, host e porta.

11. **AUTH_PASSWORD_VALIDATORS**: Validadores de senha para fortalecer a segurança das senhas de usuários.

12. **LANGUAGE_CODE e TIME_ZONE**: Configurações de internacionalização e fuso horário.

13. **STATIC_URL e STATICFILES_DIRS**: Configurações relacionadas a arquivos estáticos da aplicação, como CSS e JavaScript.

14. **DEFAULT_AUTO_FIELD**: Define o tipo de campo primário padrão para modelos.

15. **LOGGING**: Configurações de registro (logging) para monitorar e registrar eventos na aplicação.

Essas configurações são fundamentais para o funcionamento adequado da aplicação e devem ser revisadas e ajustadas conforme necessário durante o desenvolvimento e implantação.
"""

from pathlib import Path

import os


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u!cq)q6b76i)5_7i5p$a0prjz8_9%yt-(#l1&8e(m5&^l*ewl='

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Hosts/domínios permitidos para a aplicação
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dashboard'
]

# Middleware utilizados na aplicação
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Módulo que contém as configurações de URL
ROOT_URLCONF = 'project.urls'

# Configurações para renderização de templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'dashboard/templates')],
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
]

# Definindo o ponto de entrada WSGI da aplicação
WSGI_APPLICATION = 'project.wsgi.application'


# Database model
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'nome_do_banco',
        'USER': 'usuario_do_banco',
        'PASSWORD': 'senha_do_banco',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
"""

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'dashboard',
        'USER': 'BI',
        'PASSWORD': '@lphaGO',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/
# Configurações de internacionalização
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
# Configurações de arquivos estáticos
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'dashboard/static'),
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field
# Tipo de campo primário padrão para modelos
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configurações de registro (logging)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'your_app_name': {
            'handlers': ['console'],
            'level': 'ERROR',
        },
    },
}
