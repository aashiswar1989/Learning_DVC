import pandas as pd

Data = {
    {'name': 'aashish', 'age': 35, 'city': 'Nathdwara'},
    {'name': 'deepika', 'age': 33, 'city': 'Nathdwara'}
    {'name': 'radhe', 'age': 3, 'city': 'Nathdwara'}
    {'name': 'dinesh', 'age': 60, 'city': 'Nathdwara'}
    {'name': 'munna', 'age': 58, 'city': 'Nathdwara'}

}

pd.DataFrame(Data)
Data.to_csv('data/data.csv', index = False)

