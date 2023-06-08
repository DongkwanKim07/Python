import unittest
import mysql.connector
import connection as cn
# This class for Unittest that figure out this program working accurately.
# Author : Dongkwan Kim


class MyTestCase(unittest.TestCase):
    def test_connection(self):
        config = {
            'host' : 'localhost',
            'user':'Python',
            'passwd':'Python',
            'port':'3308',
            'database':"pythonproject"
        }
        # db_conn = mysql.connector.connect(**config)
        # self.assertEqual(True, db_conn)  # add assertion here


if __name__ == '__main__':
    unittest.main()
