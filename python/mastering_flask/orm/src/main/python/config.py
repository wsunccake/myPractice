class DevConfig(object):
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


class ProdConfig(object):
    pass

