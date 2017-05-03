# Set parameters for the figure:
# - size of the area of plot
# - size of the area outside the plot
# - figure title and axis labels
class Figure:

    def __init__(self,
                 title='plot',
                 xlabel='x',
                 ylabel='y',
                 width=1000,
                 height=700,
                 margin_top=50,
                 margin_bottom=70,
                 margin_left=90,
                 margin_right = 200):
        self.title = title
        self.xlabel = xlabel,
        self.ylabel = ylabel,
        self.width = width
        self.height = height
        self.margin_top = margin_top
        self.margin_bottom = margin_bottom
        self.margin_left = margin_left
        self.margin_right = margin_right