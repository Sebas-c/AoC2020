# Advent of Code - Day 4
import re

# Retrieving input file and remove first line
batchFile = open('input-Day4.txt').read().split("\n\n")

all_passport_dict = []
valid_passports = 0
valid_passports_first_rule = 0


def validate_passport(passport_to_check):
    if validate_birth_yr(passport_to_check["byr"]) and validate_issue_yr(passport_to_check["iyr"]) and \
            validate_expiration_yr(passport_to_check["eyr"]) and \
            validate_height(passport_to_check["hgt"]) and \
            validate_hair_color(passport_to_check["hcl"]) and \
            validate_eye_color(passport_to_check["ecl"]) and validate_passport_id(passport_to_check["pid"]):
        return True

    return False


def validate_birth_yr(year):
    if 1920 <= int(year) <= 2002 and re.fullmatch(r"\d{4}", year):
        return True
    return False


def validate_issue_yr(year):
    if 2010 <= int(year) <= 2020 and re.fullmatch(r"\d{4}", year):
        return True
    return False


def validate_expiration_yr(year):
    if 2020 <= int(year) <= 2030 and re.fullmatch(r"\d{4}", year):
        return True
    return False


def validate_height(height):
    if re.match(r"(\d+)(.*)", height) is not None:
        height_value, height_unit = re.fullmatch(r"(\d+)(.*)", height).groups()
        # if height is not None:
        if height_unit == "cm":
            if 150 <= int(height_value) <= 193:
                return True
            return False
        elif height_unit == "in":
            if 59 <= int(height_value) <= 76:
                return True
            return False

    return False


def validate_hair_color(hair_color):
    if re.fullmatch(r"(#)([0-9a-f]{6})", hair_color):
        return True

    return False


def validate_eye_color(eye_color):
    valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
    for color in valid_colors:
        if color == eye_color:
            return True
    return False


def validate_passport_id(passport_id):
    if re.fullmatch(r"(\d{9})", passport_id):
        return True
    return False


# Converting all passports into dict
for line in batchFile:
    # Removing random new lines in each passport
    passport_details = re.sub('\n', ' ', line)
    passport_details = passport_details.strip()
    passport_details = passport_details.split(" ")

    passport_details_dict = {}

    for detail in passport_details:
        detail = re.split(":", detail)
        if len(detail) > 0:
            passport_details_dict[detail[0]] = detail[1]
    all_passport_dict.append(passport_details_dict)

# Checking validity of passport
for passport in all_passport_dict:
    keys = passport.keys()
    if len(keys) < 8:
        if len(keys) == 7 and "cid" not in keys:
            valid_passports_first_rule += 1
            if validate_passport(passport):
                valid_passports += 1

    else:
        valid_passports_first_rule += 1
        if validate_passport(passport):
            valid_passports += 1

print("Valid passports (# of attributes only): " + str(valid_passports_first_rule))
print("Valid passports with validation: " + str(valid_passports))

# print("Total # of passports: " + str(len(all_passport_dict)))
# print(batchFile)
