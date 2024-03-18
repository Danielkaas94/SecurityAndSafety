import seaborn as sns
import matplotlib.pyplot as plt

# Example data
tips = sns.load_dataset("tips")

# Create a jointplot
sns.jointplot(x="total_bill", y="tip", data=tips)

plt.show()


# Example data
iris = sns.load_dataset("iris")

# Create a pairplot
sns.pairplot(tips)

plt.show()


