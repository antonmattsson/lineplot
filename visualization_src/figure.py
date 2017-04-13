
class Figure():

    def __init__(self,title,
                 width=500,
                 height=500,
                 margin_top=50,
                 margin_bottom=50,
                 margin_left=50):
        self.title = title
        self.width = width
        self.height = height
        self.margin_top = margin_top
        self.margin_bottom = margin_bottom
        self.margin_left = margin_left

    def set_margins(self,
                 margin_top=50,
                 margin_bottom=50,
                 margin_left=50):
        self.margin_top = margin_top
        self.margin_bottom = margin_bottom
        self.margin_left = margin_left

