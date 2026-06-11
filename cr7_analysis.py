import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/azminewasi/Kaggle-Datasets/main/CR7%20-Club%20Goals/data.csv", encoding="latin-1")

print(df.head())

print(df.columns.tolist())

"""
Graphic — Goals/Score of teams
"""
df["Team"].value_counts().plot(kind="bar", title="Goals of teams", color="steelblue")
plt.tight_layout()
plt.show()

"""
Graphic — Top-10 Opponent
"""
df["Opponent"].value_counts().head(10).plot(kind="bar", title="Top-10 Opponent", color="tomato")
plt.tight_layout()
plt.show()

"""
Graphic — Type_of_goal
"""
df["Type_of_goal"].value_counts().plot(kind="barh", title="Type_of_goal", color="steelblue")
plt.tight_layout()
plt.show()


print(
    """
    RONALDO PRIME:
    AURA MONSTER - 2008 
    Real Madrid — 450 goals 
    """
)
