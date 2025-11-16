#MapPlot.py
#Name:Nola Nelson
#Date:11/14/25
#Assignment:Lab10

import food
import pandas
import matplotlib.pyplot as plt

report = food.get_report()
proteins = []
carbohydrates = []


for stuff in report:
    protein = stuff["Data"]["Protein"]
    carbohydrate = stuff["Data"]["Carbohydrate"]
    proteins.append(protein)
    carbohydrates.append(carbohydrate)
    
    #print(protein, fat)

df = pandas.DataFrame({"Protein": proteins, "Carbohydrate": carbohydrates})
print(df)
df.plot(kind = 'scatter', x = 'Protein', y = 'Carbohydrate')

plt.savefig("output")
#This graph shows the relationship between the total amount of carbohydrates(in grams) in foods and the total amount of protein(in grams) in foods
