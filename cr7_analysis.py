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

"""
Графік — голи по командах
"""
df["Team"].value_counts().plot(kind="bar", title="Голи по командах", color="steelblue")
plt.tight_layout()
plt.show()

"""
Графік — топ-10 суперників
"""
df["Opponent"].value_counts().head(10).plot(kind="bar", title="Топ-10 суперників", color="tomato")
plt.tight_layout()
plt.show()

"""
Графік — тип голу
"""
df["Type_of_goal"].value_counts().plot(kind="barh", title="Тип голу", color="steelblue")
plt.tight_layout()
plt.show()

print(
    """
    RONALDO PRIME:
    AURA MONSTER - 2008 
    Real Madrid — 450 goals 
    """
)
