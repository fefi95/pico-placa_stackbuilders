import pytest
from ..main import validate_license


class TestClassValidLicensePlate(object):
    def test_three_numbers(self):
        assert validate_license("PBA-1231")

    def test_four_numbers(self):
        assert validate_license("PBA-123")


class TestClassInvalidLicensePlate(object):
    def test_extra_letter(self):
        with pytest.raises(ValueError):
            validate_license("ABCD-1234")

    def test_extra_number(self):
        with pytest.raises(ValueError):
            validate_license("ABCD-12345")

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

    def test_invalid_license_no_hyphen(self):
        with pytest.raises(ValueError):
            validate_license("PBA123")
