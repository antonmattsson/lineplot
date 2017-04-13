
class Legend():

    def __init__(self,plot):
        self.plot = plot
        self.parts = []
        self.n_parts = 0

    def add_part(self,part):
        self.parts.append(part)
        self.n_parts += 1

    def get_info(self):
        for i in range (0,self.n_parts):
            self.parts[i].get_info()

class LegendPart():

    def __init__(self,plotPart):
        self.plotPart = plotPart
        self.position = None

    def set_position(self,coordinates):
        self.position = coordinates

    def get_info(self):
        pass