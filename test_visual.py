import unittest
import os

from data_main import Data


class TestData(unittest.TestCase):

    def test_words(self):
        self.assertEqual(os.path.isfile(
            os.path.join(os.getcwd(), 'words',
                         'word_data.csv')), True)

    def test_data(self):
        data = Data()
        self.assertIsNotNone(data)
    """
    def test_performance(self):
        data = Data()
        self.assertIsNotNone(data.show_performance())
    """
    def test_sqlconn(self):
        data = Data()
        self.assertNotEqual(data.login, "")
        self.assertNotEqual(data.passcode, "")
        self.assertNotEqual(data.dbname, "")

    def test_sendsql(self):
        data = Data()
        self.assertIsNotNone(data.sendsql)

    def test_senddata(self):
        data = Data()
        self.assertIsNotNone(data.senddata)



