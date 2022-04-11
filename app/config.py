class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://valerochka:1@localhost/hwflask'
    SECRET_KEY = 'FGDGJSDGOEWFJqwpufwofjofj244223jejgjr'
    SECURITY_PASSWORD_SALT = 'salt'
    SECURITY_PASSWORD_HASH = 'bcrypt'
