import pandas as pd
ss = pd.read_csv('desp.csv')
print(ss)
ss
ss.describe()
ss['THICK'].value_counts()
