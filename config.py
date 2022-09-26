from msilib.schema import Class


class Config:
    DEBUG = True
    TESTING = True

    SQLALCHEMY_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI ="mysql+pymysql://root:@localhost:3306/python_blog"

class ProductionConfig(Config):
    DEBUG = False

class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    SECRET_KEY = 'MiClaveSecreta'