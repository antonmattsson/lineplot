from plot import *
import math
import numpy


class Coordinates:

    def __init__(self,x,y):
        self.x = x
        self.y = y


class LinePlot(Plot):

    def __init__(self,figure,data,plotpairs,gridon):
        super(LinePlot,self).__init__(figure,data)
        self.plotpairs = plotpairs
        self.curves = []
        self.gridon = gridon
        self.grid = None
        if self.gridon:
            self.add_grid()
        self.coordinates = None
        self.calculate_coordinates()

    def calculate_coordinates(self):
        min_x,min_y = math.inf, math.inf
        max_x, max_y = -math.inf, -math.inf
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
            x = numpy.array(self.data[self.plotpairs[i][0]])
            x_coordinates = (x-min_x) * self.figure.width/max_x
            y = numpy.array(self.data[self.plotpairs[i][1]])
            y_coordinates = (y-min_y) * self.figure.height/max_x
            self.coordinates[i] = [None] * len(x)
            for j in range(0,len(x)):
                self.coordinates[i][j] = Coordinates(x_coordinates[j],
                                                     y_coordinates[j])

    def add_grid(self):
        pass

    def add_curves(self):
        # generate colors
        for i in range(0, len(self.plotpairs)):
            pass

    def add_curve(self,plotpair):
        pass
