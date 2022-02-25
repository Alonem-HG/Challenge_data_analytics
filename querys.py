#!pip install SQLAlchemy
#!pip install psycopg2
#!pip install pandas

import os
from pathlib import Path

from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.sql import text

import connection_sqlalchemy as cs
from loggin import logging_options

# Loggers
log = logging_options.setup_logger("querys")

# Path where the script that create the tables is located
WORK_DIRECTORY = Path(os.getcwd())

SQL_LOAD_TABLES = "./sql_files/db_info_cultu_arg.sql"
SQL_VIEW_REGISTROS = "./sql_files/cantidad_registros.sql"
SQL_VIEW_CINE = "./sql_files/info_cine.sql"

file_load_tables = WORK_DIRECTORY / SQL_LOAD_TABLES
file_view_registros = WORK_DIRECTORY / SQL_VIEW_REGISTROS
file_view_cine = WORK_DIRECTORY / SQL_VIEW_CINE

# Connection with SQLAlchemy
engine_new_db = cs.simple_connection()
engine = cs.full_connection()

# query to create database
def create_db():
    with engine_new_db.connect() as conn:
        conn.execution_options(isolation_level="AUTOCOMMIT")
        dropped = conn.execute("DROP DATABASE IF EXISTS " + config('POSTGRESQL_DB'))
        conn.execute("CREATE DATABASE " + config('POSTGRESQL_DB'))
        conn.execute("commit")
        log.debug("Database was created...")


# query to load tables
def load_tables():
    with engine.connect() as conn:
        file = open(file_load_tables, 'r', encoding='utf-8')
        query = text(file.read())
        conn.execute(query)
        log.debug("Tables were created...")


def load_views_registros():
    with engine.connect() as conn:
        file = open(file_view_registros, 'r', encoding='utf-8')
        query = text(file.read())
        conn.execute(query)
        log.debug("Views of registers were created...")


def load_views_cine():
    with engine.connect() as conn:
        file = open(file_view_cine, 'r', encoding='utf-8')
        query = text(file.read())
        conn.execute(query)
        log.debug("View of cine were created...")
