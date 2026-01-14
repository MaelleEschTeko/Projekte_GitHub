
import random

GesamtRegentropfen = 1000000
CounterImKreis = 0

for i in range(GesamtRegentropfen):
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    if x*x + y*y <= 1:
        CounterImKreis += 1

Pi_Schaetzung = 4 * (CounterImKreis / GesamtRegentropfen)

print(Pi_Schaetzung)