import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("revenue.csv")

sns.lineplot(x="month",y="revenue",data=data)

plt.title("Monthly Revenue Trend")
plt.show()