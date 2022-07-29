import pandas as pd
import csv

df=pd.read_csv('merged_datset.csv')
del df["Lum"]
del df["Star_name"]
del df["Distances"]
del df["Masses"]
del df["Radiuses"]



df.to_csv('cleaned_dataset.csv')





