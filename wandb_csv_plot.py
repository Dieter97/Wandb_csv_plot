#!/usr/bin/env python3
import numpy as np
from io import StringIO
import matplotlib.pyplot as plt
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Wandb CSV matplotlib tool')
    parser.add_argument("input", help="Input .csv file from Wandb")
    parser.add_argument("-t","--type", help="Output file type", type=str, default="eps")
    parser.add_argument("-yl", "--ylabel", help="Plot Y-axis label", type=str, default="Accuracy (%)")
    parser.add_argument("-xl", "--xlabel", help="Plot X-axis label", type=str, default="Pruning Rate (%)")
    parser.add_argument("-ys", "--ysize", help="Plot Y Size", type=int, default=4)
    parser.add_argument("-xs", "--xsize", help="Plot X Size", type=int, default=5)
    parser.add_argument("-fa", "--fontaxes", help="Font Size of the axes and legend", type=int, default=11)
    parser.add_argument("-ft", "--fonttitle", help="Font Size of the title", type=int, default=13)
    parser.add_argument("-l", "--legend", help="Plot the legend", default=False, action='store_const', const=True)

    args = parser.parse_args()
    # Parse parameters
    DATA_FILE=""
    if args.input != None:
        DATA_FILE=args.input
    TITLE=DATA_FILE.replace('.csv','')

    YLABEL=args.ylabel
    XLABEL=args.xlabel
    X_SIZE=args.xsize
    Y_SIZE=args.ysize
    
    X_COLUMN_IDX=0
    Y_ROW_NAMES={}

    COLUMN_FILTER=["step","MIN","MAX"]

    DATA={}

    OUTPUT=f'{TITLE}.{args.type}'

    # Read the data first
    data_file = open(DATA_FILE, mode="r")
    data_contents = data_file.read().replace('"','')
    data_contents = data_contents.replace('#','')
    data_file.close()
    data = np.genfromtxt(StringIO(data_contents), delimiter=",", deletechars="", names=True, dtype=None, encoding=None, skip_header=False)

    # Filter the colums names
    i = 0
    for column in data.dtype.names:
        if not any(substring in column for substring in COLUMN_FILTER) and not i==X_COLUMN_IDX:
            Y_ROW_NAMES[i] = column
        i += 1

    #print(Y_ROW_NAMES)


    # Filter the and put data in vars
    for sample in data:
        for column in Y_ROW_NAMES:
            DATA[Y_ROW_NAMES[column]] = {}

    for sample in data:
        for y_column in Y_ROW_NAMES:
            if sample[y_column] == sample[y_column] and not sample[y_column] == -1: # Filter nan entries
                if sample[X_COLUMN_IDX] == sample[X_COLUMN_IDX]: # Filter nan entries
                    #data_point = { : } # {x,y}
                    DATA[Y_ROW_NAMES[y_column]][sample[X_COLUMN_IDX]] = sample[y_column]

    # Plot all data

    AXES_SIZE = args.fontaxes
    TITLE_SIZE = args.fonttitle

    plt.rc('font', size=AXES_SIZE)          # controls default text sizes
    plt.rc('axes', titlesize=AXES_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=AXES_SIZE)    # fontsize of the x and y labels
    plt.rc('xtick', labelsize=AXES_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=AXES_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=AXES_SIZE)    # legend fontsize
    plt.rc('figure', titlesize=TITLE_SIZE)  # fontsize of the figure title

    plt.figure(figsize=(X_SIZE,Y_SIZE))
    for column in DATA:
        lists = sorted(DATA[column].items()) # sorted by key, return a list of tuples
        x, y = zip(*lists) # unpack a list of pairs into two tuples
        plt.plot(x, y, label=column.split("_-_", 1)[0])

    #plt.ylim(bottom=0)
    plt.xlabel(XLABEL)
    plt.ylabel(YLABEL)
    plt.title(TITLE)
    if args.legend:
        plt.legend()
    plt.tight_layout()
    plt.savefig(OUTPUT)
    print(f'{OUTPUT} saved!')