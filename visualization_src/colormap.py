import brewer2mpl

# Create a colormap with up to 12 distinctive colours
# using colour maps from colorbrewer2.org
# Iterate over the colors using get_next_color()-method
class ColorMap:

    def __init__(self,n):
        if n < 3:
            n = 3
        if n <= 9:
            self.colors = brewer2mpl.get_map('Set1', 'Qualitative', n).colors
        elif n<= 12:
            self.colors = brewer2mpl.get_map('Paired', 'Qualitative', n).colors
        self.previous = -1

    def get_next_color(self):
        self.previous += 1
        return self.colors[self.previous]