import os

from flask import Flask
from flask_mysqldb import MySQL 


def mysql_connect(app: Flask) -> MySQL:
    app.config["MYSQL_HOST"] = os.environ["MYSQL_HOST"]
    app.config["MYSQL_USER"] = os.environ["MYSQL_USER"]
    app.config["MYSQL_PASSWORD"] = os.environ["MYSQL_PASSWORD"]
    app.config["MYSQL_DB"] = os.environ["MYSQL_DB"]
    return MySQL(app)
