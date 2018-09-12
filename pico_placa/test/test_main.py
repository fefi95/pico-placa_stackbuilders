from datetime import datetime
import pytest
import sys
import unittest
from ..main import main

class TestClassMain(unittest.TestCase):
    """Checks the argv given to the main and its outputs"""
    def test_valid_main_can_drive(self):
        sys.argv = ["main.py", "ABC-1234", "10/09/2018", "7:30PM"]
        with pytest.raises(SystemExit) as e:
            main()
        assert e.value.code == 0

    def test_valid_main_can_not_drive(self):
        sys.argv = ["main.py", "ABC-4321", "10/09/2018", "7:00PM"]
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

    def test_invalid_date1(self):
        sys.argv = ["main.py", "ABC-1234", "10/13/2018", "7:30PM"]
        with pytest.raises(SystemExit) as e:
            main()
        assert e.value.code == -3

    def test_invalid_date2(self):
        sys.argv = ["main.py", "ABC-1234", "10-09-2018", "7:30PM"]
        with pytest.raises(SystemExit) as e:
            main()
        assert e.value.code == -3

    def test_invalid_time1(self):
        sys.argv = ["main.py", "ABC-1234", "10/09/2018", "7:30P"]
        with pytest.raises(SystemExit) as e:
            main()
        assert e.value.code == -3

    def test_invalid_time2(self):
        sys.argv = ["main.py", "ABC-1234", "10/09/2018", "17:30AM"]
        with pytest.raises(SystemExit) as e:
            main()
        assert e.value.code == -3
