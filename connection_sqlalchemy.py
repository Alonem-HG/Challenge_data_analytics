from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.sql import text

from loggin import logging_options

# Loggers
log = logging_options.setup_logger("connection_sqlalchemy")

# Connection with SQLAlchemy


def simple_connection():
    engine_new_db = create_engine(config('DIALECT')+"://"+config('POSTGRESQL_USER')+":"+config('POSTGRESQL_PASSWORD')+"@" +
                                  config('POSTGRESQL_HOST')+"/")
    log.debug("Connection simple successfully....")
    return engine_new_db


def full_connection():
    engine = create_engine(config('DIALECT')+"://"+config('POSTGRESQL_USER')+":"+config('POSTGRESQL_PASSWORD')+"@" +
                           config('POSTGRESQL_HOST')+"/"+config('POSTGRESQL_DB'))
    log.debug("Connection full successfully....")
    return engine
