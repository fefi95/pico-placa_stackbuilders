from datetime import datetime
import unittest
from ..main import can_drive


class TestClassCanDrive(unittest.TestCase):
    """Tests if a given car's license plate can drive."""
    def setUp(self):
        self.license = "ABC-4321"

    def test_banned_day_morning_before(self):
        date_time = datetime(2018, 9, 10, 6, 59)
        assert can_drive(self.license, date_time)

    def test_banned_day_morning_after(self):
        date_time = datetime(2018, 9, 10, 9, 31)
        assert can_drive(self.license, date_time)

    def test_banned_day_afternoon_before(self):
        date_time = datetime(2018, 9, 10, 15, 59)
        assert can_drive(self.license, date_time)

    def test_banned_day_afternoon_after(self):
        date_time = datetime(2018, 9, 10, 19, 31)
        assert can_drive(self.license, date_time)

    def test_not_banned_day(self):
        date_time = datetime(2018, 9, 11, 19, 30)
        assert can_drive(self.license, date_time)

    def test_weekend(self):
        date_time = datetime(2018, 9, 15, 19, 30)
        assert can_drive(self.license, date_time)

class TestClassCanNotDrive(unittest.TestCase):
    """Tests if a given car's license plate can not drive."""
    def setUp(self):
        self.license = "ABC-4321"

    def test_banned_day_morning_start(self):
        date_time = datetime(2018, 9, 10, 7, 00)
        assert not can_drive(self.license, date_time)

    def test_banned_day_morning_end(self):
        date_time = datetime(2018, 9, 10, 9, 30)
        assert not can_drive(self.license, date_time)

    def test_banned_day_afternoon_start(self):
        date_time = datetime(2018, 9, 10, 16, 00)
        assert not can_drive(self.license, date_time)

    def test_banned_day_afternoon_end(self):
        date_time = datetime(2018, 9, 10, 19, 30)
        assert not can_drive(self.license, date_time)
