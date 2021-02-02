# Wandb_CSV_Plot Tool

This is a command line python tool to create customizable matplotlibs from wandb generated data files (csv format).

## Usage

First make sure the dependecies are installed:

```
pip install -r requirement.txt
```

Tool help: 
```
usage: wandb_csv_plot.py [-h] [-t TYPE] [-yl YLABEL] [-xl XLABEL] [-ys YSIZE] [-xs XSIZE] input

Wandb CSV matplotlib tool

positional arguments:
  input                 Input .csv file from Wandb

optional arguments:
  -h, --help            show this help message and exit
  -t TYPE, --type TYPE  Output file type
  -yl YLABEL, --ylabel YLABEL
                        Plot Y-axis label
  -xl XLABEL, --xlabel XLABEL
                        Plot X-axis label
  -ys YSIZE, --ysize YSIZE
                        Plot Y Size
  -xs XSIZE, --xsize XSIZE
                        Plot X Size
```