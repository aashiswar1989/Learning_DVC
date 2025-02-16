import pandas as pd
from pathlib import Path


def save_data(df):
    data_dir = Path('data')
    if not data_dir.is_dir():
        data_dir.mkdir(parents=True, exist_ok=True)

    file_path = data_dir/'data.csv'
    df.to_csv(file_path, index = False)
    print(f'Data file saved to {file_path}')

def create_data():

    # create a sample DatFrame 
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [23, 32, 26],
        'City': ['New York', 'Seattle', 'California']
    }

    df = pd.DataFrame(data)

    save_data(df)

    # Adding new row to dataframe
    new_data = {'Name': 'Robert', 'Age': 55, 'City': 'Boston'}
    df.loc[len(df.index), :] = new_data
    save_data(df)

    new_data2 = {'Name': 'Alex', 'Age': 60, 'City': 'New York'}
    df.loc[len(df.index), :] = new_data2
    save_data(df)

if __name__ == '__main__':
    create_data()