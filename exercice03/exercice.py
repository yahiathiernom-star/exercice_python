temperatures = [12.5, 14, 9.5, 17, 21, 19.5, 11]
print("moyenne :", round(sum(temperatures)/len(temperatures), 2))
print("température min :", min(temperatures))
print("température max :", max(temperatures))
nbrsup = 0
for temperature in temperatures:
    if temperature > 15:
        nbrsup += 1
print("nombre de jours où la température est supérieure à 15°C :", nbrsup)
temperatures_fahrenheit = [(temperature * 9/5) + 32 for temperature in temperatures]
for temperature in temperatures:
    faratemp = (temperature * 9/5) + 32
    print(faratemp)
for i, temperature in enumerate(temperatures):
    print("jour", i + 1, ":", temperature, "°C")







           