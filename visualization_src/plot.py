
class Plot:

    def __init__(self,figure,data):

        self.figure = figure
        self.parts = []
        self.data = data

class PlotPart:

    def __init__(self,label,color):

        self.label = label
        self.color = color


class Curve(PlotPart):

    def __init__(self, points, label, color):
        self.points = points
        super(Curve, self).__init__(label,color)
