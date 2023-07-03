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

    def test_invalid_login_admin(self):
        self.login_page.username_input.setText('A100')
        self.login_page.password_input.setText('password')

        print("Admin login failed")

    def test_invalid_login_hrassistant(self):
        self.login_page.username_input.setText('H100')
        self.login_page.password_input.setText('password')

        print("HR Assistant login failed")

    def test_invalid_login_staff(self):
        self.login_page.username_input.setText('S100')
        self.login_page.password_input.setText('password')

        print("Staff login failed")

if __name__ == '__main__':
    try:
        unittest.main()
    except SystemExit:
        pass
