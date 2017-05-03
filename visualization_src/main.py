from figure import *
from data_reader import *
from lineplotdrawer import *
from lineplot import *

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QComboBox, QPushButton
import sys


class Controls(QWidget):

    def __init__(self,parent):
        super().__init__(parent)

        font = QFont()
        font.setPixelSize(15)

        dim_label = QLabel('Choose dimensions',self)
        dim_label.setFont(font)
        dim_label.move(0,50)

        self.dim_choice = QComboBox(self)
        self.dim_choice.addItems(['1D', '2D'])
        self.dim_choice.move(0,80)

        walker_label = QLabel('Choose number of walkers',self)
        walker_label.setFont(font)
        walker_label.move(0,140)

        self.walker_choice = QComboBox(self)
        self.walker_choice.addItems(['1', '2', '3'])
        self.walker_choice.move(0,170)

        button = QPushButton('Update plot',self)
        button.move(0,250)
        button.clicked.connect(self.on_click)

        self.show()

    def on_click(self):

        dim = str(self.dim_choice.currentText())
        walkers = str(self.walker_choice.currentText())
        self.parent().update_plot(dim,walkers)



class myapp(QWidget):

    def __init__(self):
        super().__init__()
        self.plot = None
        self.initUI()

    def initUI(self):

        self.grid = QGridLayout()
        self.setLayout(self.grid)

        data = DataReader('../data/rw2d.csv').read_to_dict()
        fig = Figure('Random walks','','')
        pairs = []
        lplot = LinePlot(fig,data,pairs)
        self.plot = LinePlotDrawer(lplot,self)

        self.grid.addWidget(self.plot,1,1,5,6)

        controls = Controls(self)
        self.grid.addWidget(controls,1,8,5,1)


        self.setGeometry(100,100,
                         fig.width + fig.margin_left + fig.margin_right+ 300,
                         fig.height + fig.margin_top + fig.margin_bottom + 50)
        self.show()

    def update_plot(self,dim,walkers):

        if dim == '1D':
            data = DataReader('../data/rw1d.csv').read_to_dict()
            fig = Figure('1D Random walks','time','distance')
            pairs = {
                '1': [['time', 'rw1']],
                '2': [['time', 'rw1'], ['time', 'rw2']],
                '3': [['time', 'rw1'], ['time', 'rw2'], ['time', 'rw3']]}[walkers]



        if dim == '2D':
            data = DataReader('../data/rw2d.csv').read_to_dict()
            fig = Figure('2D Random walks', 'x', 'y')
            pairs = {
                '1': [['x1','y1']],
                '2': [['x1','y1'],['x2','y2']],
                '3': [['x1','y1'],['x2','y2'],['x3','y3']]}[walkers]


        lplot = LinePlot(fig, data, pairs)



        self.grid.removeWidget(self.plot)
        self.plot.deleteLater()
        self.plot = None

        self.plot = LinePlotDrawer(lplot, self)
        self.grid.addWidget(self.plot, 1, 1, 5, 6)


def main():

    app = QApplication(sys.argv)

    m = myapp()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()