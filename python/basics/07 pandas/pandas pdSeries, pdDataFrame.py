import pandas as pd
import numpy as np

arr = np.random.rand(4,4)
pd.DataFrame(arr)
print(arr)

df = pd.DataFrame(np.random.rand(8, 4), columns=list('ABCD'))
df.head()
print(df)

d = {'fst': pd.Series(np.random.rand(3), index=list('abc')),
     'snd': pd.Series(np.random.rand(4), index=list('abcd'))}
df = pd.DataFrame(d)
print(df)