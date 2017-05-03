from math import inf, floor, log10
from numpy import arange, array

from plot import *
from colormap import *

# A coordinate class
class Coordinates:

    def __init__(self,x,y):
        self.x = x
        self.y = y


# The main class of line plots
# Input:
#       - figure : Figure
#       - data : dict
#       - plotpairs : list of pairs of variables to be plotted
#       - gridon : boolean indicating if grid is included or not

# Transforms the values of points to Coordinates
# Calculates good places for axis ticks
class LinePlot(Plot):

    def __init__(self, figure ,data, plotpairs, curve_labels = None, gridon=True):
        super(LinePlot,self).__init__(figure,data)
        self.plotpairs = plotpairs
        self.curve_labels = curve_labels
        self.curves = []
        self.colormap = ColorMap(len(plotpairs))
        self.gridon = gridon
        self.grid = None
        self.coordinates = None
        self.x_ticks = None
        self.y_ticks = None
        self.x_tick_labels = []
        self.y_tick_labels = []
        if len(plotpairs):
            self.calculate_coordinates()
            self.add_curves()

    # transforms the numbers of original units to pixels (Coordinates)
    # fits all points to figure width and height = plot area
    def calculate_coordinates(self):
        min_x, min_y = inf, inf
        max_x, max_y = -inf, -inf
        for i in range(0,len(self.plotpairs)):
            temp_min_x = min(self.data[self.plotpairs[i][0]])
            temp_max_x = max(self.data[self.plotpairs[i][0]])
            temp_min_y = min(self.data[self.plotpairs[i][1]])
            temp_max_y = max(self.data[self.plotpairs[i][1]])
            if temp_min_x < min_x:
                min_x = temp_min_x
            if temp_max_x > max_x:
                max_x = temp_max_x
            if temp_min_y < min_y:
                min_y = temp_min_y
            if temp_max_y > max_y:
                max_y = temp_max_y

        self.coordinates = [None] * len(self.plotpairs)
        for i in range(0, len(self.plotpairs)):
            x = array(self.data[self.plotpairs[i][0]])
            x_coordinates = (x-min_x) * (self.figure.width-20)/(max_x-min_x) + self.figure.margin_left + 10
            y = array(self.data[self.plotpairs[i][1]])
            y_coordinates = (y-max_y) * (self.figure.height-20)/(min_y-max_y) + self.figure.margin_top + 10
            self.coordinates[i] = [None] * len(x)
            for j in range(0,len(x)):
                self.coordinates[i][j] = Coordinates(x_coordinates[j],
                                                     y_coordinates[j])

        # Transfrom ticks into coordinates
        xticks = self.calculate_ticks(min_x,max_x)
        for tick in xticks:
            self.x_tick_labels.append(str(tick))
        self.x_ticks = array(xticks)
        self.x_ticks = (self.x_ticks-min_x) * (self.figure.width-20)/(max_x-min_x) + self.figure.margin_left + 10
        self.xticks = list(self.x_ticks)

        yticks = self.calculate_ticks(min_y, max_y)
        for tick in yticks:
            self.y_tick_labels.append(str(tick))
        self.y_ticks = array(yticks)
        self.y_ticks = (self.y_ticks - max_y) * (self.figure.height-20)/(min_y-max_y) + self.figure.margin_top + 10
        self.y_ticks = list(self.y_ticks)

    # Creates good spacing for axis ticks
    # the plots have 6-7 ticks on both axes
    def calculate_ticks(self,min_x,max_x):
        dif = (max_x - min_x) / 5
        pow10 = pow(10, floor(log10(dif)))
        if pow10 == 0:
            step = round(dif)
        elif pow10 < 0:
            step = pow10 * round(dif / pow10)
        else:
            step = pow10 * round(dif / pow10)
        start = step * floor(min_x/step)
        end = step * floor(max_x/step)
        ticks = list(arange(start, end, step))
        ticks.append(end)
        if ticks[0] < min_x:
            ticks.pop(0)
        if ticks[-1] + step == max_x:
            ticks.append(max_x)
        return ticks

    # Every variable pair has its own Curve object
    # Unless curve labels are specified, labels will be names of y variables
    def add_curves(self):
        for i in range(0, len(self.coordinates)):
            if self.curve_labels is not None:
                label = self.curve_labels[i]
            else:
                label = self.plotpairs[i][1]
            curve = Curve(self.coordinates[i],label,self.colormap.get_next_color())
            self.curves.append(curve)
