import numpy as np
from io import StringIO
import matplotlib.pyplot as plt

DATA_FILE="PARAMETERS.csv"
TITLE=DATA_FILE.replace('.csv','')
YLABEL="PARAMETERS"
XLABEL="Pruning Rate(%)"
X_ROW_NAMES={"Pruning_Rate_(%)" : 0}
Y_ROW_NAMES={}
COLUMN_FILTER=["step","MIN","MAX"]

DATA={}

X_SIZE=7
Y_SIZE=5

# Read the data first
data_file = open(DATA_FILE, mode="r")
data_contents = data_file.read().replace('"','')
data_file.close()
data = np.genfromtxt(StringIO(data_contents), delimiter=",", names=True, deletechars='"', dtype=None, encoding=None)

# Filter the colums names
i = 0
for column in data.dtype.names:
    if not any(substring in column for substring in COLUMN_FILTER) and not any(substring in column for substring in X_ROW_NAMES):
        Y_ROW_NAMES[i] = column
    i += 1

print(Y_ROW_NAMES)


# Filter the and put data in vars
for sample in data:
    for column in Y_ROW_NAMES:
        DATA[Y_ROW_NAMES[column]] = {}

for sample in data:
    for y_column in Y_ROW_NAMES:
        if sample[y_column] == sample[y_column] and not sample[y_column] == -1: # Filter nan entries
            for column in X_ROW_NAMES:
                if sample[X_ROW_NAMES[column]] == sample[X_ROW_NAMES[column]]: # Filter nan entries
                    #data_point = { : } # {x,y}
                    DATA[Y_ROW_NAMES[y_column]][sample[X_ROW_NAMES[column]]] = sample[y_column]

# Plot all data
plt.figure(figsize=(X_SIZE,Y_SIZE))
for column in DATA:
    lists = sorted(DATA[column].items()) # sorted by key, return a list of tuples
    x, y = zip(*lists) # unpack a list of pairs into two tuples
    plt.plot(x, y, label=column)

plt.ylim(bottom=0)
plt.xlabel(XLABEL)
plt.ylabel(YLABEL)
plt.title(TITLE)
plt.legend()
plt.savefig(f'output/{TITLE}.pdf')