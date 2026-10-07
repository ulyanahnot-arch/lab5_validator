import unittest
from src.string_validator.validator import Validator, ValidationError

class TestStringValidator(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()

    def test_valid(self):
        self.assertTrue(self.validator.validate("()"))
        self.assertTrue(self.validator.validate("<div><p>{ test }</p></div>"))

    def test_invalid(self):
        with self.assertRaises(ValidationError):
            self.validator.validate("<div><p>{ test }}</p</div>")

if __name__ == "__main__":
    unittest.main()