from datetime import datetime, time
import re
import sys


DATETIME_FORMAT = "%d/%m/%Y %I:%M%p"
LICENSE_PATTERN = "[A-Z]{3}-\d{3,4}"
BANNED_LICENSES = [("1","2"), ("3","4"), ("5","6"), ("7","8"), ("9","0"), (), () ]
MORNING_RANGE = (time(7, 00), time(9, 30))
AFTERNOON_RANGE = (time(16, 00), time(19,30))

def validate_license(license_plate):
    is_correct = re.fullmatch(LICENSE_PATTERN, license_plate)
    if (is_correct is None):
        raise ValueError("The license plate format is no correct.")
    return is_correct


def can_drive(license_plate, date_time):
    last_number = license_plate[-1:]
    is_banned = last_number in BANNED_LICENSES[date_time.weekday()]
    time = date_time.time()
    return is_banned and \
        ((time >= MORNING_RANGE[0] and time <= MORNING_RANGE[1]) or \
        (time >= AFTERNOON_RANGE[0] and time <= AFTERNOON_RANGE[1]) )

def main():
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
        print(date_time)
    except ValueError as e:
        print("The date or time format is no correct.")
        exit()

    print(can_drive(license_plate, date_time))


if __name__ == "__main__":
    main()
