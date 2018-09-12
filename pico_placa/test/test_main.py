from datetime import datetime
import pytest
import sys
import unittest
from ..main import main

class TestClassMain(unittest.TestCase):
    """Checks the argv given to the main and its outputs"""
    def test_valid_main(self):
        sys.argv = ["main.py", "ABC-1234", "10/09/2018", "7:30PM"]
        with pytest.raises(SystemExit) as e:
            main()
        assert e.value.code == 0

    def test_missing_arg(self):
        sys.argv = ["main.py", "10/09/2018", "7:30PM"]
        with pytest.raises(SystemExit) as e:
            main()
        assert e.value.code == -1

    def test_extra_arg(self):
        sys.argv = ["main.py", "ABC-1234", "10/09/2018", "7:30PM", "extra"]
        with pytest.raises(SystemExit) as e:
            main()
        assert e.value.code == -1

    def test_invalid_license(self):
        sys.argv = ["main.py", "ABCD-1234", "10/09/2018", "7:30PM"]
        with pytest.raises(SystemExit) as e:
            main()
        assert e.value.code == -2

    def test_invalid_date(self):
        sys.argv = ["main.py", "ABC-1234", "10/13/2018", "7:30PM"]
        with pytest.raises(SystemExit) as e:
            main()
        assert e.value.code == -3

    def test_invalid_date(self):
        sys.argv = ["main.py", "ABC-1234", "10/09/2018", "7:30P"]
        with pytest.raises(SystemExit) as e:
            main()
        assert e.value.code == -3
