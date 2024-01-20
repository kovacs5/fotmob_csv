import pandas as pd

df = pd.DataFrame({'name': ['Raphael', 'Donatello'],
                   'mask': ['red', 'purple'],
                   'weapon': ['sai', 'bo staff']})
  
df.to_csv('https://github.com/kovacs5/fotmob_csv/blob/main/out.csv')
