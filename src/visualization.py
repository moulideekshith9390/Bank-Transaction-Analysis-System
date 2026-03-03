import matplotlib.pyplot as plt
import seaborn as sns

def plot_category_spending(category_data):
    plt.figure()
    category_data.plot(kind="bar")
    plt.title("Spending by Category")
    plt.ylabel("Total Amount")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_monthly_spending(monthly_data):
    plt.figure()
    monthly_data.plot()
    plt.title("Monthly Spending Trend")
    plt.ylabel("Total Amount")
    plt.tight_layout()
    plt.show()

def plot_clusters(df):
    plt.figure()
    sns.scatterplot(data=df, x=df.index, y="Amount", hue="Cluster")
    plt.title("Spending Clusters")
    plt.show()