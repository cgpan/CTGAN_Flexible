from ctgan import CTGAN
from ctgan import load_demo
import os

# get the path of the current file
print(os.getcwd())

real_data = load_demo()
print(real_data.head())

# Names of the columns that are discrete
discrete_columns = [
    'workclass',
    'education',
    'marital-status',
    'occupation',
    'relationship',
    'race',
    'sex',
    'native-country',
    'income'
]


ctgan = CTGAN(epochs=10, cuda=True)
ctgan.fit(real_data, discrete_columns)

# Create synthetic data
synthetic_data = ctgan.sample(1000)