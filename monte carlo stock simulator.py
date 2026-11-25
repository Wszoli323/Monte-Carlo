import yfinance
import numpy as np
import matplotlib.pyplot as plt
dane = yfinance.Ticker("AAPL").history(period="1mo")
zmiany = dane["Close"].pct_change().dropna()
srednia = zmiany.mean()
odchylenie = zmiany.std()
ostatnia = dane["Close"].iloc[-1]
cena = ostatnia
wynik = []
for _ in range(10000):
    cena = ostatnia
    for _ in range(1):
        zmiana = np.random.normal(srednia, odchylenie)
        cena = cena * (1 + zmiana)
    wynik.append(cena)

np.array(wynik)

porównanie = np.array(wynik) > ostatnia

percentyle = np.percentile(wynik, [5, 50, 95])
print(f"W 90% przypadków cena akcji AAPL po dniu będzie w przedziale od {percentyle[0]:.2f} do {percentyle[2]:.2f}, mediana wyniesie {percentyle[1]:.2f}, a w {np.mean(porównanie) * 100:.2f}% przypadków cena będzie wyższa niż obecna cena {ostatnia:.2f}.")

plt.hist(wynik, bins=100, edgecolor='black')
plt.title("Symulacja Monte Carlo dla akcji AAPL")
plt.axvline(ostatnia)
plt.show()


