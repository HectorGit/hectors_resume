
import os

class Config(object):
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgresql://postgres:postgres@localhost:5432/my_resume_db' 
    # DEACTIVATED
    # API_ROUTE = os.environ.get('API_ROUTE') or 'http://localhost:5001'
    FLASK_CONFIG =  os.environ.get('FLASK_CONFIG') or 'localhost'
    ASSETS_AUTO_BUILD = True
    ASSETS_DEBUG = False
    # COMPRESS_MIMETYPES = ['text/html', 'text/css', 'text/xml', 'application/json', 'application/javascript','font/eot','font/opentype','font/otf', 'image/bmp', 'image/svg+xml','image/vnd.microsoft.icon', 'image/jpeg', 'image/png']
    # COMPRESS_LEVEL = 6
    # COMPRESS_MIN_SIZE = 500
    # RECAPTCHA_SITE_KEY='6LeZc6gbAAAAAKrKLipf8-NUvEAQWeQyu0z09roN'
    # RECAPTCHA_SECRET_KEY='6LeZc6gbAAAAAJ5kszf36JyDZCvpgf24_U13SnBy'