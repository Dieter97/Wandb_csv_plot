# Wandb_CSV_Plot Tool

This is a command line python tool to create customizable matplotlibs from wandb generated data files (csv format).

## Usage

First make sure the dependecies are installed:

```
pip install -r requirement.txt
```

Tool help: 
```
python wandb_csv_plot.py -h
usage: wandb_csv_plot.py [-h] [-t TYPE] [-yl YLABEL] [-xl XLABEL] [-ys YSIZE] [-xs XSIZE] [-fa FONTAXES] [-ft FONTTITLE] [-l] input

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
  -fa FONTAXES, --fontaxes FONTAXES
                        Font Size of the axes and legend
  -ft FONTTITLE, --fonttitle FONTTITLE
                        Font Size of the title
  -l, --legend          Plot the legend
```

Examples:

```
python3 wandb_csv_plot.py Accuracy_vs_Parameters.csv -yl "Accuracy (%)" -xl "PARAMETERS" -t pdf
python3 wandb_csv_plot.py Conv_Layer_32.csv -t svg -fa 12 -l
```