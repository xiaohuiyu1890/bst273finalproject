"""
==============================
BST 273 Final Project, 100 points
==============================

NAME: Xiaohui Yu
EMAIL: xiaohuiyu@hsph.harvard.edu

"""

import argparse
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


"""
Step #1: set up command-line interface
"""

description = """
A script for generating scatter plots based on columns
of data from TSV-format input files.
"""

parser = argparse.ArgumentParser( description=description )
parser.add_argument(
    "input_file",
    help="path to the input data file (TSV format)",
)

parser.add_argument(
    "-x",
    "--x",
    type=int,
    default=1,
    help="1-based index of the column containing continuous x-values to plot",
)

parser.add_argument(
    "-y",
    "--y",
    type=int,
    default=1,
    help="1-based index of the column containing continuous y-values to plot",
)

parser.add_argument(
    "-cat", # by convention, command line options with a single - are one letter
    "--category",
    type=int,
    default=None,
    help="1-based index of the column containing categorical “series” values on which to stratify (optional: if not specified, plot all x- and y-values as one series).",
)

parser.add_argument(
    "-output", # same comment as above
    "--output",
    default=None,
    help="Path to the output file (optional: if not specified, save the plot with a reasonable default name in the working directory).",
)

args = parser.parse_args( )


"""
Step #2: load data of columns (x, y) and convert to floats
"""
def column(path, index=1):
    c = []
    fh = open(path)
    for line in fh:
        row = line.strip( ).split( "\t" )
        c.append(row[index-1])
    fh.close( )
    return c

xoverall = column(args.input_file, args.x)
yoverall = column(args.input_file, args.y)


xlabel = xoverall[0]
xstring=xoverall[1:]
x = []
for xitem in xstring:
    x.append(float(xitem))

ylabel = yoverall[0]
ystring=yoverall[1:]
y = []
for yitem in ystring:
    y.append(float(yitem))


"""
Step #3: create an optional stratified plot by category
"""
df = pd.DataFrame()
df['x'] = x
df['y'] = y

if args.category is not None:
    category = column(args.input_file, args.category)
    categorylabel=category[0]
    category=category[1:]
    df['category'] = category
    sns.lmplot('x', 'y', data=df, fit_reg=False, hue="category", legend=None)
    plt.legend(title=categorylabel)
else:
    sns.lmplot('x', 'y', data=df, fit_reg=False, legend=None)


"""
Step #4: customize the plot (legent, title)
"""


plt.xlabel(xlabel)
plt.ylabel(ylabel)
figtitle=xlabel + " vs " + ylabel
plt.title("A Scatter Plot of " + figtitle)



"""
Step #5: save scatter plot to optional or default output path
"""

if args.output is not None:
    plt.savefig(args.output)
else:
    plt.savefig("scatter_plot.png") # you could have put this in as the default for the --output arg instead
