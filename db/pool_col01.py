import time
from db import db_config
import psycopg2
from psycopg2 import pool 
import logging

col01_pool = psycopg2.pool.ThreadedConnectionPool(2, 5, user = db_config.col01_db_user,
                                                        password = db_config.col01_db_pw,
                                                        host = db_config.col01_db_host,
                                                        port = db_config.col01_db_port,
                                                        database = db_config.col01_db_name)
logging.debug("Conectada BD")

def getCursorCol01():
    con = col01_pool.getconn()
    cur = con.cursor()
    return cur 

def releaseConnCol01(conn):
    col01_pool.putconn(conn)
