from io import StringIO
import requests
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style('whitegrid')
url = "http://elections.huffingtonpost.com/pollster/2012-general-election-romney-vs-obama.csv"
source = requests.get(url).text
poll_data = StringIO(source)
poll_df = pd.read_csv(poll_data)
poll_sort_df = poll_df[['Pollster', 'Partisan', 'Affiliation']].sort_values(
    'Pollster').drop_duplicates()


def select_affiliation(affiliation):
    if affiliation == 'Dem':
        return 'Obama'
    elif affiliation == 'Rep':
        return 'Romney'
    else:
        return 'None'


poll_sort_df['Affiliation'] = poll_sort_df['Affiliation'].apply(
    select_affiliation)
sns.countplot('Affiliation', data=poll_sort_df)
