import os


class Config:
    """
    general configuration parent class
    """

    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://benie:12345@localhost/sixty'
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    UPLOADED_PHOTOS_DEST = 'app/static/photos'
