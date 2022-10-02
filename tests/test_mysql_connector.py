import unittest

from flask import Flask

from app.db import mysql_connect


class TestMySQL(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)

    def test_mysql_connect(self):
        with self.app.app_context():
            mysql_connect(self.app)

    def test_mysql_cursor_simple_select(self):
        with self.app.app_context():
            mysql = mysql_connect(self.app)
            cur = mysql.connection.cursor()
            cur.execute("select 1 from dual")
            result = cur.fetchone()[0]
            self.assertEqual(result, 1)

    def test_mysql_cursor_select_from_user_profile_table(self):
        with self.app.app_context():
            mysql = mysql_connect(self.app)
            cur = mysql.connection.cursor()
            cur.execute("select * from user_profile")
            results = cur.fetchall()
