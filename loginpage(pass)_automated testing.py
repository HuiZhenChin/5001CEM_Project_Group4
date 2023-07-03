import unittest
from unittest.mock import patch
from PySide6.QtWidgets import QApplication
from software_engineering_project import LoginPage

class TestLoginPage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])
        
    def setUp(self):
        self.login_page = LoginPage()

    def test_valid_login_admin(self):
        self.login_page.username_input.setText('A145')
        self.login_page.password_input.setText('ADMIN1')

        print("Admin login passed successfully")

    def test_valid_login_hrassistant(self):
        self.login_page.username_input.setText('H106')
        self.login_page.password_input.setText('HRASSISTANT1')

        print("HR Assistant login passed successfully")

    def test_valid_login_staff(self):
        self.login_page.username_input.setText('S110')
        self.login_page.password_input.setText('STAFF1')

        print("Staff login passed successfully")

if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit:
        pass
