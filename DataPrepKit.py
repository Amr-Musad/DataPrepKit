import pandas as pd
import numpy as np

def read_csv(file_path):
    return pd.read_csv(file_path)

def read_excel(file_path):
    return pd.read_excel(file_path)

def read_json(file_path):
    return pd.read_json(file_path)

def data_summary(data):
    avg_values = np.mean(data, axis=0)
    most_frequent_values = data.mode().iloc[0]
    return avg_values, most_frequent_values

def handle_missing_values(data, strategy='remove'):
    if strategy == 'remove':
        return data.dropna()
    elif strategy == 'impute':
        return data.fillna(data.mean())

def encode_categorical(data):
    return pd.get_dummies(data)


