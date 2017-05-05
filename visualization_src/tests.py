import unittest
from data_reader import *
from figure import *
from lineplot import *


class TestReader(unittest.TestCase):

    def setUp(self):
        self.path = '../data/'

    # classic case, float columns
    def test_correct_file(self):
        file = self.path + 'xy.csv'
        d = DataReader(file).read_to_dict()

        self.assertEqual(list(range(1,6)), d['x'])
        self.assertEqual(list(range(2,11,2)), d['y'])
        self.assertTrue(type(d['x'][0]) is float)
        self.assertTrue(type(d['y'][0]) is float)

    # One of columns is a string
    def test_string_column(self):
        file = self.path + 'groups.csv'
        d = DataReader(file).read_to_dict()
        keys = list(d.keys())
        keys.sort()

        self.assertEqual(keys, ['group','score'])
        self.assertTrue(type(d['group'][0]) is str)
        self.assertTrue(type(d['score'][0]) is float)

    def test_invalid_rows(self):

        with self.assertRaisesRegexp(ReadingError,'number of values on row'):
            file = self.path + '3inrow.csv'
            DataReader(file).read_to_dict()

        with self.assertRaisesRegexp(ReadingError,'number of values on row'):
            file = self.path + 'blankrow.csv'
            DataReader(file).read_to_dict()


class TestLinePlot(unittest.TestCase):

    def setUp(self):
        self.path = '../data/'
        file = self.path + 'twopairs.csv'
        self.data = DataReader(file).read_to_dict()
        self.pairs = []
        self.pairs.append(['x','y'])
        self.pairs.append(['x2', 'y2'])
        fig = Figure(margin_left=40, margin_top=40)
        self.lplot = LinePlot(fig, self.data, self.pairs)

    def test_coordinate_calculation(self):

        predicted_coordinates1 = [Coordinates(50, 163+1/3),
                                  Coordinates(213+1/3, 446+2/3),
                                  Coordinates(376+2/3, 560),
                                  Coordinates(540, 333+1/3),
                                  Coordinates(703+1/3, 503+1/3)]
        predicted_coordinates2 = [Coordinates(213+1/3, 730),
                                  Coordinates(376+2/3, 220),
                                  Coordinates(703+1/3, 390),
                                  Coordinates(866+2/3, 220),
                                  Coordinates(1030, 50)]


        for i in range(0, len(predicted_coordinates1)):
            self.assertAlmostEqual(predicted_coordinates1[i].x, self.lplot.coordinates[0][i].x)
            self.assertAlmostEqual(predicted_coordinates1[i].y, self.lplot.coordinates[0][i].y)

            self.assertAlmostEqual(predicted_coordinates2[i].x, self.lplot.coordinates[1][i].x)
            self.assertAlmostEqual(predicted_coordinates2[i].y, self.lplot.coordinates[1][i].y)

    def test_curve_creation(self):
        curves = self.lplot.curves
        self.assertEqual(len(curves),2)
        self.assertTrue(curves[0].label == 'y' or curves[0].label == 'y2')
        self.assertTrue(curves[1].label == 'y' or curves[1].label == 'y2')



if __name__ == "__main__":
    unittest.main()
