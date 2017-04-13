import unittest
from data_reader import *

class TestReader(unittest.TestCase):

    def setUp(self):
        self.path = '../data/'

    def test_correct_file(self):
        file = self.path + 'xy.csv'
        d = DataReader(file).read_to_dict()

        self.assertEqual(['x','y'], d['header'])

        self.assertEqual(list(range(1,6)), d['x'])
        self.assertEqual(list(range(2,11,2)), d['y'])
        self.assertTrue(type(d['x'][0]) is float)
        self.assertTrue(type(d['y'][0]) is float)

    def test_invalid_input(self):
        f = self.path + 'invalid.csv'

        with self.assertRaisesRegexp(ReadingError,'column type'):
            DataReader(f,'weird')

    def test_string_column(self):
        file = self.path + 'groups.csv'
        d = DataReader(file,x_type='string').read_to_dict()

        self.assertTrue(type(d['x'][0]) is str)
        self.assertTrue(type(d['y'][0]) is float)

    def test_invalid_rows(self):

        with self.assertRaisesRegexp(ReadingError,'number of values on row'):
            file = self.path + '3inrow.csv'
            DataReader(file).read_to_dict()

        with self.assertRaisesRegexp(ReadingError,'number of values on row'):
            file = self.path + 'blankrow.csv'
            DataReader(file).read_to_dict()

if __name__ == "__main__":
    unittest.main()
