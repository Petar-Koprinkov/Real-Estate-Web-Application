from django.core.exceptions import ValidationError
from unittest import TestCase
from real_estate_web_application.common.validators import BadLanguageValidator


class TestBadWordValidator(TestCase):
    def setUp(self):
        self.bad_words = ["bad_word", "offensive"]

    def test__bad_word__raises_validation_error(self):
        validator = BadLanguageValidator(words=self.bad_words)
        with self.assertRaises(ValidationError) as ve:
            validator('This is a bad_word!')

        self.assertEqual(str(ve.exception), "['Please DO Not use bad language']")

    def test__bad_word__custom_error_message(self):
        custom_message = "Custom error message!"
        validator = BadLanguageValidator(words=self.bad_words, message=custom_message)
        with self.assertRaises(ValidationError) as context:
            validator("This contains offensive language!")

        self.assertEqual(str(context.exception), "['Custom error message!']")
