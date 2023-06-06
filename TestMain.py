import unittest
from main import try_creds
class TestCredentialVerification(unittest.TestCase):
    def test_granting_valid(self):
        self.assertEqual(try_creds({"admin": "admin"}, "admin", "admin"), True)
    def test_not_granting_invalid_password(self):
        self.assertEqual(try_creds({"admin": "admin"}, "admin", "admins"), False)
    def test_not_granting_invalid_user(self):
        self.assertEqual(try_creds({"admin": "admin"}, "sadmin", "admin"), False)

if __name__ == '__main__':
    unittest.main()
