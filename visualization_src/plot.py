# Parent of all plot classes
class Plot:

    def __init__(self,figure,data):

        self.figure = figure
        self.parts = []
        self.data = data


# Parent of all plotpart classes
class PlotPart:

    def __init__(self,label,color):

        self.label = label
        self.color = color


# Line plot consists of curves
class Curve(PlotPart):

    def __init__(self, points, label, color):
        self.points = points
        super().__init__(label,color)
