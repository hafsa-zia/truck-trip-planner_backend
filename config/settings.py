MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]

INSTALLED_APPS = [
    ...
    'rest_framework',
    'corsheaders',
    'trips',
]

CORS_ALLOW_ALL_ORIGINS = True