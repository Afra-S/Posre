from re import T
import pandas as pd
import numpy as np
df = pd.read_csv('posre_Protein_back_250.itp', skiprows=3, delimiter="\s+")
df2 = df[';i'] - 4142
df[';i'] = df2
df4 = df.replace(';i', df2)
print(df4)
df.to_csv(r'posre_Protein_back_250_2.itp', header=True, index=False, sep='$', mode='a')

#Have to delete the space between ;i, and add the title by yourself in the end and replace $ by 7 spaaces.
