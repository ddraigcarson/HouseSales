import numpy as np
from functools import partial

ID = "id"
PRICE = "price"
DATE_OF_TRANSFER = "data_of_transfer"
POSTCODE = "postcode"
PROPERTY_TYPE = "property_type"
OLD_NEW = "old_new"
DURATION = "duration"
PAON = "paon"
SAON = "saon"
STREET = "street"
LOCALITY = "locality"
TOWN_CITY = "town_city"
DISTRICT = "district"
COUNTY = "county"
PPD = "ppd"

column_names = [
    ID, PRICE, DATE_OF_TRANSFER, POSTCODE, PROPERTY_TYPE, OLD_NEW, DURATION,
    PAON, SAON, STREET, LOCALITY, TOWN_CITY, DISTRICT, COUNTY, PPD
]

enum_property_type = ('D', 'S', 'T', 'F', 'O')
enum_old_new = ('Y', 'N')
enum_duration = ('F', 'L')
enum_ppd = ('A', 'B')


def validate_exists(item):
    if item is None:
        return False
    else:
        return True


def validate_not_empty(item):
    if len(item.strip()) == 0:
        return False
    else:
        return True


def validate_id_format(item):
    if item[1] != '{' and item[-1] != '}':
        return False
    else:
        return True


def validate_item_in_enum(enum, item):
    if item in enum:
        return True
    else:
        return False


def validate_is_number(item):
    try:
        float(item)
    except (ValueError, TypeError):
        return False
    else:
        return True


def validate_is_date_format(item):
    if item[4] != '-' or item[7] != '-':
        return False
    elif not validate_is_number(item[0:4]) \
            or not validate_is_number(item[5:7]) \
            or not validate_is_number(item[8:10]):
        return False
    else:
        return True


column_validations = dict([
    (ID,                [validate_exists, validate_not_empty, validate_id_format]),
    (PRICE,             [validate_exists, validate_is_number]),
    (DATE_OF_TRANSFER,  [validate_exists, validate_not_empty, validate_is_date_format]),
    (POSTCODE,          [validate_exists, validate_not_empty]),
    (PROPERTY_TYPE,     [partial(validate_item_in_enum, enum_property_type)]),
    (OLD_NEW,           [partial(validate_item_in_enum, enum_old_new)]),
    (DURATION,          [partial(validate_item_in_enum, enum_duration)]),
    (PPD,               [partial(validate_item_in_enum, enum_ppd)])
])


def validate_data_set(data_set):
    invalid_rows = []
    for key, value in column_validations.items():
        if key in data_set:
            for i, item in data_set[key].iteritems():
                for validator in value:
                    valid = validator(item)
                    if not valid:
                        invalid_rows.append(i)
                        break
    return invalid_rows
