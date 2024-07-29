import seaborn as sns
import matplotlib.pyplot as plt

var = [1, 2, 3, 4, 5]
var1 = [2, 3, 4, 5, 6]

data = plt.Dataframe({'var':var, 'var1':var1 })

sns.lineplot(x = 'var', y = 'var1', data = data)
plt.show() 