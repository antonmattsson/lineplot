# lineplot
A project work for a basic programming course. The goal was to create a tool for drawing lineplots of numerical data.

-- For more detailed doumentation see docs (only in Finnish) --

The tool can be used from Python's command line by importing line_plot function from command_line.py
The parameters are as follows:

line_plot(file,
	  pairs,
	  title = 'Plot',
	  xlabel = 'x axis',
	  ylabel = 'y axis',
	  curve_labels = None,
	  gridon=True)

The file should be a .csv file with every variable on its own column, equal number of observations per variable and no missing values.
pairs is a 2-dimensional list of pairs of variables that should be plotted. A curve is drawn for each pair.

Example:

line_plot('../data/rw2d.csv',
	  [['x1','y1'],['x2','y2'],['x3','y3']],
	  'Random walk 2D',
	  'x',
	  'y',
	  curve_labels=['walker 1','walker 2','walker 3'])

The main.py file includes a small application showcasing the tool by drawing lineplots of random walks.