import kagglehub
import pandas as pd

# Download latest version
path = kagglehub.dataset_download("venky73/spam-mails-dataset")

print("Path to dataset files:", path)

df = pd.read_csv(str(path)+r'\spam_ham_dataset.csv')

import os
os.makedirs(r"C:\DATA SCIENCE and ANALITICS\email spam\data\rawdata",exist_ok=True)

df.to_csv(r"C:\DATA SCIENCE and ANALITICS\email spam\data\rawdata\raw.csv",index=False)

print("Raw data stored succe.....")

