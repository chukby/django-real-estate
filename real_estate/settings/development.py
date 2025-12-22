from .base import *  # noqa


DATABASES = {
    "default": {
        "ENGINE": env("POSTGRES_ENGINE", default="django.db.backends.postgresql"),
        "NAME": env("POSTGRES_NAME", default="real_estate_dev"),
        "USER": env("POSTGRES_USER", default="real_estate_user"),
        "PASSWORD": env("POSTGRES_PASSWORD", default="real_estate_password"),
        "HOST": env("POSTGRES_HOST", default="localhost"),  
        "PORT": env("POSTGRES_PORT", default="5432"),
    }
}   