import unittest
class UserTestCase1(unittest.TestCase):
    def setUp(self):
        print("==setup==")

    def test_name(self):
        print("==teardown==")

    def tearDown(self):
        print("==teardown==")


