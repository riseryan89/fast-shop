import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "PASSWORD": os.getenv("DB_PW"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
        "OPTIONS": {"autocommit": True, "charset": "utf8mb4"},
    }
}

ST_API = os.getenv("ST_API")
EMAIL_ID = os.getenv("EMAIL_ID")
EMAIL_PW = os.getenv("EMAIL_PW")
