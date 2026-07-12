DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME', 'portfolio_db'),
        'USER': os.getenv('DB_USER', 'salmon_admin'),
        'PASSWORD': os.getenv('DB_PASSWORD'),  # Bu yerda os.getenv bo'lishi shart!
        'HOST': os.getenv('DB_HOST', '127.0.0.1'),
        'PORT': os.getenv('DB_PORT', '5432'),
    }
}
