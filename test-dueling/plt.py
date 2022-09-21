import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('dueling-reward.csv')

print(df.head())
X = df['RET']
plt.plot(X)
plt.show()