python3 wandb_csv_plot.py PARAMETERS.csv -yl "PARAMETERS" -t pdf
python3 wandb_csv_plot.py FLOPS.csv -yl "FLOPs" -t pdf
python3 wandb_csv_plot.py Accuracy_vs_FLOPs.csv -yl "Accuracy (%)" -xl "FLOPs" -t pdf
python3 wandb_csv_plot.py Accuracy_vs_Parameters.csv -yl "Accuracy (%)" -xl "PARAMETERS" -t pdf
python3 wandb_csv_plot.py Accuracy_vs_Pruning_Rate.csv -t svg