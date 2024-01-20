import pandas as pd
import os

df = pd.DataFrame({'name': ['Raphael', 'Donatello'],
                   'mask': ['red', 'purple'],
                   'weapon': ['sai', 'bo staff']})3

os.makedirs('csv', exist_ok=True)  
df.to_csv('csv/out.csv')
