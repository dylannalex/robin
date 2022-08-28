import os
from robin.database import database
from mysql.connector.connection_cext import CMySQLConnection


def setup_tables(db: CMySQLConnection):
    script_dir = os.path.dirname(__file__)
    database.execute_script(db, os.path.join(script_dir, "scripts/create_tables.sql"))
    database.execute_script(db, os.path.join(script_dir, "scripts/setup_tasks.sql"))


def setup_database():
    db = database.connect()
    setup_tables(db)


if __name__ == "__main__":
    setup_database()
