import numpy as np
import pandas as pd

df = pd.DataFrame(np.random.randn(6, 4), columns=list('ABCD'))
print(df)
print(df[df.C > 0])
