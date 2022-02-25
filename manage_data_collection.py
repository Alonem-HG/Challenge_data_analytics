import pandas as pd
import connection_sqlalchemy as cs
from sqlalchemy import create_engine

from decouple import config
from loggin import logging_options

log = logging_options.setup_logger("data_normalization")

#database = config('POSTGRESQL_DB')
TABLA_CULTURAL = 'info_cultural'
TABLA_CINE = 'info_cine'

class Manage_data():
    
    def insert_data(self):
        #engine = create_engine('postgresql://postgres:Proot@localhost:5432/' +database)
        engine = cs.full_connection()
        conn = engine.connect()

        df_completo = pd.read_csv("data_complete/2022-02/info_completa.csv")
        df_cine = pd.read_csv("data_complete/2022-02/info_cine.csv")

        df_completo.to_sql(TABLA_CULTURAL, conn, if_exists = 'append', index = False)
        df_cine.to_sql(TABLA_CINE, conn, if_exists = 'append', index = False)
        log.info("All data was inserted in the database")
