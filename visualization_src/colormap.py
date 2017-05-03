import brewer2mpl


class ColorMap:

    def __init__(self,n):
        if n < 3:
            n = 3
        self.colors = brewer2mpl.get_map('Set1', 'Qualitative', n).colors
        self.previous = -1

    def get_next_color(self):
        self.previous += 1
        return self.colors[self.previous]