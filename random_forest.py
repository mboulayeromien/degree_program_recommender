import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder

df = pd.read_csv('alevel_categorical.csv')
df = df.fillna(0)
rep = {
    'A':5, 'B':4, 'C':3, 'D':2, 'E':1, 'F':0, 'U':0, 'X':0, 'S':0
}
df = df.replace(rep)
df['Establishment'] = LabelEncoder().fit_transform(df['Establishment'])


