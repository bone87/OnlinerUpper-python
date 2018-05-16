import unittest
from selenium import webdriver


class UpperRunner(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path='')

    def tearDown(self):
        super(UpperRunner, self).tearDown()

    def run(self):
        pass
