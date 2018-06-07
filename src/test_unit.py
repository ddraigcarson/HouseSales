import unittest
import pandas as pd
import src.sale_data_set as sds


class SaleDataSetTestCase(unittest.TestCase):

    def test_validate_id_column(self):
        d = {'id': ['{123A-456B-789C}', '{123A-456B-789C}', '{123A-456B-789C}', '', '123A-456B']}
        df = pd.DataFrame(d)
        valid_rows, invalid_rows = sds.validate_id_column(df['id'])
        self.assertEqual(2, len(invalid_rows))
        self.assertEqual(3, len(valid_rows))

    def test_validate_property_type_column(self):
        d = {'property_type': ['D', 'S', 'T', 'F', 'O', '', None]}
        df = pd.DataFrame(d)
        valid_rows, invalid_rows = sds.validate_column_with_set_values(df['property_type'], ['D', 'S', 'T', 'F', 'O'])
        self.assertEqual(2, len(invalid_rows))
        self.assertEqual(5, len(valid_rows))

    def test_validate_data_set(self):
        d = {'property_type': ['D', 'S', 'T', 'F', 'O', '', None]}
        df = pd.DataFrame(d)
        sds.validate_data_set(df)