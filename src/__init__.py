import pandas as pd
from os import path
import src.sale_data_set as sds


def load_csv(file, names=None, coverters=None, data_types=None):
    if path.isfile(file):
        print("Loading file {0}, with dtypes: {1}".format(file, data_types))
        dataset = pd.read_csv(file, names=names, converters=coverters, index_col=False, dtype=data_types)
        return dataset
    else:
        print("File does not exist: {0}".format(file))


def save_sales_to_db():
    print("Saving sales data to db")
    ds = load_csv("../resources/pp-2018.csv", names=sds.column_names)
    sds.validate_id_column(ds['id'])
    print(ds['id'])


def run():
    print("----- Starting -----")
    save_sales_to_db()


if __name__ == '__main__':
    run()