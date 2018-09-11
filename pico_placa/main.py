from datetime import datetime, time
import re
import sys


DATETIME_FORMAT = "%d/%m/%Y %I:%M%p"
LICENSE_PATTERN = "[A-Z]{3}-\d{3,4}"
BANNED_LICENSES = [("1","2"), ("3","4"), ("5","6"), ("7","8"), ("9","0"), (), ()]
MORNING_RANGE = (time(7, 00), time(9, 30))
AFTERNOON_RANGE = (time(16, 00), time(19,30))

def validate_license(license_plate):
    """
    Determines whether a license plate has a valid pattern or not.

    @param license_plate: the license plate
    Raises an error if the license is not valid. Returns True otherwise.
    """
    is_correct = re.fullmatch(LICENSE_PATTERN, license_plate)
    if (is_correct is None):
        raise ValueError("The license plate format is no correct.")
    return is_correct


def can_drive(license_plate, date_time):
    """
    Checks if a car can drive at a given date and time.

    @param license_plate: the license plate of the car.
    @param date_time: the date and time to check.
    Returns True if can drive. False otherwise.
    """
    last_number = license_plate[-1:]
    is_banned = last_number in BANNED_LICENSES[date_time.weekday()]

    if (is_banned):
        time = date_time.time()
        is_banned = ((time >= MORNING_RANGE[0] and time <= MORNING_RANGE[1]) or \
            (time >= AFTERNOON_RANGE[0] and time <= AFTERNOON_RANGE[1]) )
    return not is_banned

def main():
    if (len(sys.argv) != 4):
        print("USAGE: python main.py <license_plate> <dd/mm/YYYYY> <h:mmAM/PM>")
        exit()

    license_plate = sys.argv[1]
    date = sys.argv[2]
    time = sys.argv[3]

    try:
        validate_license(license_plate)
    except ValueError as e:
        print(e)
        exit()
    try:
        date_time = datetime.strptime("%s %s" % (date, time), DATETIME_FORMAT)
    except ValueError as e:
        print("The date or time format is not correct.")
        exit()

    message = "The car with the license plate %s can "% (license_plate)
    if (can_drive(license_plate, date_time)):
        message += "drive on %s at %s" % (date, time)
    else:
        message += "not drive on %s at %s" % (date, time)
    print(message)

if __name__ == "__main__":
    main()
