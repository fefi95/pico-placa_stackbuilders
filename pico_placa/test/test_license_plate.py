import pytest
import unittest
from ..main import validate_license


class TestClassValidLicensePlate(unittest.TestCase):
    """Test that the given license plate is valid."""
    def test_three_numbers(self):
        assert validate_license("PBA-1231")

    def test_four_numbers(self):
        assert validate_license("PBA-123")


class TestClassInvalidLicensePlate(unittest.TestCase):
    """Test that the given license plate is not valid and raises an exception"""
    def test_extra_letter(self):
        with pytest.raises(ValueError):
            validate_license("ABCD-1234")

    def test_extra_number(self):
        with pytest.raises(ValueError):
            validate_license("ABC-12345")

    def test_mixed_letters(self):
        with pytest.raises(ValueError):
            validate_license("ABC-A23")
        with pytest.raises(ValueError):
            validate_license("1BC-123")

    def test_lowercase(self):
        with pytest.raises(ValueError):
            validate_license("PbA-123")

    def test_mixed_lowercase(self):
        with pytest.raises(ValueError):
            validate_license("ABC-a23")

    def test_no_hyphen(self):
        with pytest.raises(ValueError):
            validate_license("PBA123")
