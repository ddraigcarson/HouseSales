import unittest
import pandas as pd
import src.sale_data_set as sds


class SaleDataSetTestCase(unittest.TestCase):

    def test_validate_id_column(self):
        d = {sds.ID: [' ', '123A-456B', '{123A-456B-789C}', '{123A-456B-789C}', '{123A-456B-789C}']}
        df = pd.DataFrame(d)
        invalid_rows = sds.validate_data_set(df)
        self.assertEqual(2, len(invalid_rows))
        self.assertEqual([0, 1], invalid_rows)

    def test_validate_price_column(self):
        d = {sds.PRICE: ['asd', None, 12000, 15000, 9999.9]}
        df = pd.DataFrame(d)
        invalid_rows = sds.validate_data_set(df)
        self.assertEqual(2, len(invalid_rows))
        self.assertEqual([0, 1], invalid_rows)

    def test_validate_date_column(self):
        d = {sds.DATE_OF_TRANSFER: [
            None,
            '',
            '201-01-08 00:00',
            '2011-1-08 00:00',
            '2011-1-8 00:00',
            '2018-01-08 00:00'
        ]}
        df = pd.DataFrame(d)
        invalid_rows = sds.validate_data_set(df)
        self.assertEqual(5, len(invalid_rows))
        self.assertEqual([0, 1, 2, 3, 4], invalid_rows)

    def test_validate_postcode_column(self):
        d = {sds.POSTCODE: [None, '', 'CF35 5PJ']}
        df = pd.DataFrame(d)
        invalid_rows = sds.validate_data_set(df)
        self.assertEqual(2, len(invalid_rows))
        self.assertEqual([0, 1], invalid_rows)

    def test_validate_property_type_column(self):
        d = {sds.PROPERTY_TYPE: ['', None, float('nan'), 'D', 'S', 'T', 'F', 'O']}
        df = pd.DataFrame(d)
        invalid_rows = sds.validate_data_set(df)
        self.assertEqual(3, len(invalid_rows))
        self.assertEqual([0, 1, 2], invalid_rows)

    def test_validate_old_new_column(self):
        d = {sds.OLD_NEW: ['', None, float('nan'), 'Y', 'N']}
        df = pd.DataFrame(d)
        invalid_rows = sds.validate_data_set(df)
        self.assertEqual(3, len(invalid_rows))
        self.assertEqual([0, 1, 2], invalid_rows)

    def test_validate_duration_column(self):
        d = {sds.DURATION: ['', None, float('nan'), 'F', 'L']}
        df = pd.DataFrame(d)
        invalid_rows = sds.validate_data_set(df)
        self.assertEqual(3, len(invalid_rows))
        self.assertEqual([0, 1, 2], invalid_rows)

    def test_validate_ppd_column(self):
        d = {sds.PPD: ['', None, float('nan'), 'A', 'B']}
        df = pd.DataFrame(d)
        invalid_rows = sds.validate_data_set(df)
        self.assertEqual(3, len(invalid_rows))
        self.assertEqual([0, 1, 2], invalid_rows)
