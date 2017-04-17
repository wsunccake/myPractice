class Config(object):
    SECRET_KEY = '736670cb10a600b695a55839ca3a5aa54a7d7356cdef815d2ad6e19a2031182b'


class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.sqlite3'


class DevConfig(Config):
    DEBUG = True

    # sqlite
    SQLALCHEMY_DATABASE_URI = 'sqlite:///database.sqlite3'

    # mysql
    # SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@ip:port/db_name'

    # postgre
    # SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://user:password@ip:port/db_name'

    # mssql
    # SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://user:password@ip:port/db_name'

    # oracle
    # SQLALCHEMY_DATABASE_URI = 'oracle+xc_oracle://user:password@ip:port/db_name'

    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
