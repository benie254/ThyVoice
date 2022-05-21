import os


class Config:
    """
    general configuration parent class
    """

    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://benie:12345@localhost/thyvoice'
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    # email config_options
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'davinci.monalissa3@gmail.com'
    # MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    MAIL_PASSWORD = 'beenieman'
    SUBJECT_PREFIX = 'thePitcher'
    SENDER_EMAIL = 'davinci.monalissa3@gmail.com'


class ProdConfig(Config):
    """
    production configuration child class
    """

    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://benie:12345@localhost/thyvoice'
    
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")  # the only problem with this is that it connects to heroku's postgres, which has since been updated by sqlalchemy to be postgresql. The logic in the line with replace, if you check closely, is that it requests heroku to change the name from postgres:// to instead include ql at the end, so that it reads postgresql://
    #  another line that could work well to replace postgres with postgresql is this: os.environ.get('DATABASE_URL?sslmode=require').replace('postgres://', 'postgresql://')

    DEBUG = True


class DevConfig(Config):
    """
    development configuration child class
    """

    DEBUG = True

    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://benie:12345@localhost/thyvoice'


config_options = {
'development':DevConfig,
'production':ProdConfig
}