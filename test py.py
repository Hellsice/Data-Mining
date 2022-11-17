import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (11,8)


df = pd.DataFrame({'x' : range(1,101)}).assign(y = lambda d: 10*d.x -0.2*(d.x)**2 + np.random.normal(0.0, 100, 100))
df.head()


sns.scatterplot(x="x", y="y", data=df)
plt.show()



sns.scatterplot(x="y", y="x", data=df)
plt.show()

