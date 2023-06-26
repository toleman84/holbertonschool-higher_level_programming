#!/usr/bin/pytohn3
"""_summary_
"""
import unittest
from models import base
Base = base.Base
import pep8


class TestBase(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    def test_pep8(self):
        """_summary_
        """
        style = pep8.StyleGuide()
        filenames = ['models/base.py']
        check = style.check_files(filenames)
        self.assertEqual(check.total_errors, 0, 'PEP8 style errors: %d' % check.total_errors)


class TestBase(unittest.TestCase):
    def test_id_given(self):
        """Test ids match when given"""
        self.assertTrue(Base(999), self.id == 999)
        self.assertTrue(Base(0), self.id == 0)
        self.assertTrue(Base(1), self.id == 1)
        self.assertTrue(Base(-80), self.id == -80)

if __name__ == "__main__":
    unittest.main()
