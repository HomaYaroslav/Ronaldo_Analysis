import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("https://raw.githubusercontent.com/azminewasi/Kaggle-Datasets/main/CR7%20-Club%20Goals/data.csv", encoding="latin-1")

print(df.head())

print(df.columns.tolist())

print("Всього голів:", len(df))
print("Найбільше за команду:", df["Team"].value_counts().idxmax())
print("Найбільше в турнірі:", df["Competition"].value_counts().idxmax())
print("Найчастіший тип голу:", df["Type_of_goal"].value_counts().idxmax())
print("Топ-5 суперників:\n", df["Opponent"].value_counts().head(5))
print("Вдома:", df["Venue"].value_counts()["H"], "| На виїзді:", df["Venue"].value_counts()["A"])
print("Найкращий сезон:", df["Season"].value_counts().idxmax(), df["Season"].value_counts().max(), "голів")
print("Пропуски:\n", df.isnull().sum())

# """
# Graphic — Goals/Score of teams
# """
# df["Team"].value_counts().plot(kind="bar", title="Goals of teams", color="steelblue")
# plt.tight_layout()
# plt.show()

# """
# Graphic — Top-10 Opponent
# """
# df["Opponent"].value_counts().head(10).plot(kind="bar", title="Top-10 Opponent", color="tomato")
# plt.tight_layout()
# plt.show()

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
