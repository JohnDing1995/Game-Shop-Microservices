class Config(object):
    DEBUG = True
    TESTING = False
    DATABASE_URI = 'sqlite:///user.db'
    JWT_EXP_DELTA_MINS = 30
    JWT_SECRET = 'thesecretoflogin'
    JWT_ALGORITHM = 'HS256'
    ENCRYPT_ROUND = 6
