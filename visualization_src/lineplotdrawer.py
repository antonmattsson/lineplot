from qtclasses import *
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QLabel

# Draw a line plot using helper classes from qtclasses.py
class LinePlotDrawer(QWidget):

    def __init__(self,lineplot,parent=None):
        super().__init__(parent)
        self.plot = lineplot
        self.h = None
        self.w = None

        self.initFigure()
        self.draw_title_labels()
        if len(self.plot.plotpairs):
            self.draw_axes()
            self.draw_lines_legend()

        self.show()

    def initFigure(self):

        figure = self.plot.figure
        w = figure.width + figure.margin_left + figure.margin_right
        h = figure.height + figure.margin_top + figure.margin_bottom
        self.w = w
        self.h = h
        self.setGeometry(50,50,w,h)

        PlotBackGround(figure.margin_left, figure.margin_top, figure.width, figure.height, self)

    def draw_title_labels(self):
        figure = self.plot.figure
        font = QFont()
        font.setPixelSize(30)

        title = QLabel(figure.title, self)
        title.setFont(font)
        title.move(round(self.w / 2 - title.width() / 2), 5)

        font.setPixelSize(20)

        xlab = QLabel(figure.xlabel[0],self)
        xlab.setFont(font)
        xlab.move(round(figure.width/2-xlab.width()/2+figure.margin_left),self.h-35)

        ylab = VerticalLabel(figure.ylabel[0],self)
        ylab.setFont(font)
        ylab.move(5,round(self.h/2-ylab.height()/2))

    def draw_axes(self):
        figure = self.plot.figure

        # ---- x-axis ----
        Line(Coordinates(figure.margin_left,self.h-figure.margin_bottom),
             Coordinates(self.w-figure.margin_right,self.h-figure.margin_bottom),
             width = 1,
             parent = self)

        # x axis ticks
        font = QFont()
        font.setPixelSize(15)
        for i in range(0,len(self.plot.x_ticks)):
            start = Coordinates(self.plot.x_ticks[i],self.h-figure.margin_bottom)
            end = Coordinates(self.plot.x_ticks[i],self.h-figure.margin_bottom + 10)
            Line(start, end, width=1, parent=self)
            if self.plot.gridon:
                Line(start,Coordinates(start.x,figure.margin_top),1,[220,220,220],self)
            lab = QLabel(self.plot.x_tick_labels[i],self)
            lab.setFont(font)
            lab.move(self.plot.x_ticks[i]-10,self.h-figure.margin_bottom + 10)

        # --- y-axis ---
        Line(Coordinates(figure.margin_left, self.h - figure.margin_bottom),
             Coordinates(figure.margin_left,figure.margin_top),
             width=1,
             parent=self)

        # y axis ticks
        for i in range(0,len(self.plot.y_ticks)):
            start = Coordinates(figure.margin_left,self.plot.y_ticks[i])
            end = Coordinates(figure.margin_left - 10,self.plot.y_ticks[i])
            Line(start, end, width=1, parent=self)
            if self.plot.gridon:
                Line(start,Coordinates(self.w-figure.margin_right,start.y),1,[220,220,220],self)
            lab = QLabel(self.plot.y_tick_labels[i], self)
            lab.setFont(font)
            lab.setAlignment(Qt.AlignRight)
            lab.move(figure.margin_left-50,self.plot.y_ticks[i]-10)

    # draw the actual lines to the plot and add corresponding legend
    def draw_lines_legend(self):
        figure = self.plot.figure
        legend_pos = Coordinates(figure.margin_left + figure.width + 10,figure.margin_top +10)
        font = QFont()
        font.setPixelSize(15)

        for curve in self.plot.curves:
            # Draw lines
            for i in range(1,len(curve.points)):
                Line(curve.points[i-1],curve.points[i],color = curve.color, parent = self)

            # Draw legend
            legend_line_end = Coordinates(legend_pos.x + 30, legend_pos.y)
            Line(legend_pos,legend_line_end,color = curve.color, parent = self)
            lab = QLabel(curve.label,self)
            lab.setFont(font)
            lab.move(legend_pos.x+ 40,legend_pos.y-12)

            legend_pos = Coordinates(legend_pos.x,legend_pos.y+30)

