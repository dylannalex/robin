import mysql.connector
from urllib.parse import urlparse
from robin.settings import CLEARDB_DATABASE_URL
from datetime import datetime

from mysql.connector.connection_cext import CMySQLConnection
from mysql.connector.errors import OperationalError
from typing import Callable


"""
Database functions for accessing database and run sql
scripts
"""


def connect() -> CMySQLConnection:
    dbc = urlparse(CLEARDB_DATABASE_URL)
    db = mysql.connector.connect(
        host=dbc.hostname,
        user=dbc.username,
        database=dbc.path.lstrip("/"),
        passwd=dbc.password,
    )
    return db


def database_access(function: Callable):
    def wrapper(db: CMySQLConnection, *args):
        while True:
            try:
                return function(db, *args)
            except OperationalError:
                db.reconnect()
            except Exception as exception:
                print(
                    f"[DATABASE] Could not run function {function.__name__}",
                    f"Error: {exception}",
                    sep="\n",
                )
                return

    return wrapper


@database_access
def execute_script(db: CMySQLConnection, filename: str):
    # Open and read the file as a single buffer
    fd = open(filename, "r")
    sql_file = fd.read()
    fd.close()
    sql_commands = sql_file.split(";")
    # Run commands in sql file
    cursor = db.cursor()
    for command in sql_commands:
        cursor.execute(command)
    db.commit()


"""
Database functions for adding new users and task logs
instances
"""


@database_access
def add_tgm_user(db: CMySQLConnection, username: str, first_name: str, id: int):
    # Open and read the file as a single buffer
    cursor = db.cursor()
    cursor.execute(
        f"INSERT INTO tgm_user (username, first_name, id)\
        VALUES ('{username}', '{first_name}', {id});"
    )
    db.commit()


@database_access
def add_task_log(
    db: CMySQLConnection,
    task_start: datetime,
    task_end: datetime,
    user_id: int,
    task_id: int,
):
    # Open and read the file as a single buffer
    cursor = db.cursor()
    cursor.execute(
        f"INSERT INTO task_log (task_start, task_end, user_id, task_id)\
        VALUES ('{task_start}', '{task_end}', {user_id}, {task_id});"
    )
    db.commit()


"""
Database functions for checking if an instance exists
"""


@database_access
def is_tgm_user_added(db: CMySQLConnection, user_id: int):
    cursor = db.cursor()
    cursor.execute(f"SELECT * FROM tgm_user WHERE id={user_id};")
    return len([user for user in cursor])
