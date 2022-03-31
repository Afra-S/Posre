from re import T
import pandas as pd
import numpy as np
df = pd.read_csv('rmsd.xvg', skiprows=18, delimiter="\s+")
print(df)
df2 = df['time']*0.001
print(df2)
df3= df2.round(2)
df3.to_csv(r'rmsd_time.dat', header=True, index=False, sep=' ', mode='a')
df4= (df['RMSD']*10).round(2)
print(df4)
print(df3, df4)
df4.to_csv(r'rmsd_rmsd.dat', header=True, index=False, sep=' ', mode='a')
bigdata = pd.concat([df3, df4], axis=1)
bigdata.to_csv(r'rmsd_data.dat', header=True, index=False, sep='$', mode='a')

