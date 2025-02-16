import pandas as pd
from pathlib import Path


# create a sample DatFrame 
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [23, 32, 26],
    'City': ['New York', 'Seattle', 'California']
}

df = pd.DataFrame(data)
data_dir = Path('data')

if not data_dir.is_dir():
    data_dir.mkdir(parents=True, exist_ok=True)

file_path = data_dir/'data.csv'
df.to_csv(file_path, index = False)
print(f'Data file saved to {file_path}')