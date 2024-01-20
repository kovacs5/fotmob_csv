import pandas as pd

df = pd.DataFrame({'name': ['Raphael', 'Donatello'],
                   'mask': ['red', 'purple'],
                   'weapon': ['sai', 'bo staff']})
  
df.to_csv('https://github.com/kovacs5/fotmob_csv/blob/9300862180c56edb00c7b88d0998fc129ba3911f/out.csv')
