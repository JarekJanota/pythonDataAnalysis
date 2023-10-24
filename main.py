import pandas as pd
import matplotlib.pyplot as plt
import json
from colorama import Fore

#odczyt json i wyświetlenie w konsoli danych
file_path = 'data.json'
df = pd.read_json(file_path)
print(df.to_string())

#wyświetlenie maksymalnego pulsu
max_pulse = df["Maxpulse"].max()
print(f"Maksymalny puls (Maxpulse): {max_pulse}")

#wykres 1
ax = df.plot(y=["Maxpulse"], kind="bar", color="red")
df.plot(kind='bar', y=["Pulse"], color='green', ax=ax, title='maksymalny/aktualny puls')

#wykres 2
df.plot(kind='bar', y=["Pulse", "Maxpulse"], cmap='cividis', title='maksymalny/aktualny puls')

#zakres osi Y do maxa + 10 oczek wyżej, przeskok co 20 oczek
plt.yticks(range(0, df["Maxpulse"].max() + 10, 20))
ax.set_yticks(range(0, df[["Pulse", "Maxpulse"]].max().max() + 10, 20))

# Obrócenie etykiet na pionowo
ax.set_xticklabels(ax.get_xticklabels(), rotation=0)
plt.xticks(rotation='horizontal')

#wyświetlenie wykresów
plt.show()
