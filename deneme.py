import os
import pandas as pd
from datetime import datetime

def write_attendance():
  user = input()
  path = "./generated_files/" + user + '/'

  if not os.path.exists(path):
    os.makedirs(path)

  now = datetime.now()
  date = now.strftime("%Y-%m-%d")
  time = now.strftime("%H:%M:%S")

  ym = now.strftime("%Y-%m")
  fn = path + user + '-' + ym + '.csv'

  if not os.path.exists(fn):
    df = pd.DataFrame(columns=['Reg. No.', 'Date', 'Time'])
    df.to_csv(fn, index=False)

  df = pd.read_csv(fn)
  lst = df['Date'].tolist()

  if date in lst:
    print('You have already gave your attendance.')
  else:
    df.loc[len(df)] = [user, date, time]
    df.to_csv(fn, index=False)
    print('Your attendance has been updated.')
    print('{}'.format(df))


if __name__ == '__main__':
  write_attendance()
