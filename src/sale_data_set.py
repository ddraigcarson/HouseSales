import numpy as np


column_names = [
    "id", "price", "data_of_transfer", "postcode", "property_type",
    "old_new", "duration", "paon", "saon", "street", "locality",
    "town_city", "district", "county", "ppd"
]


def validate_id_column(col):
    print("Validating the ID Column")
    valid_rows = []
    invalid_rows = []

    for i, item in col.iteritems():
        if item is None:
            invalid_rows.append(i)
        elif len(item) == 0:
            invalid_rows.append(i)
        elif item[1] != '{' and item[-1] != '}':
            invalid_rows.append(i)
        else:
            valid_rows.append(i)

    return valid_rows, invalid_rows


def validate_column_with_set_values(col, values):
    valid_rows = []
    invalid_rows = []

    for i, item in col.iteritems():
        if item in values:
            valid_rows.append(i)
        else:
            invalid_rows.append(i)
    return valid_rows, invalid_rows


column_validations = dict([
    ("id", [validate_id_column]),
    ("property_type", [validate_column_with_set_values])
])


def validate_property_type_column(col):
    print("Validating the property type column")
    valid_rows = []
    invalid_rows = []

    for i, item in col.iteritems():
        if item in ['D', 'S', 'T', 'F', 'O']:
            valid_rows.append(i)
        else:
            invalid_rows.append(i)
    return valid_rows, invalid_rows


def validate_data_set(data_set):
    for key, value in column_validations.items():
        print(key)