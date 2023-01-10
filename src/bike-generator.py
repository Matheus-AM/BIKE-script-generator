import pandas as pd
import random

data = []
for id in range(9,879):
    elem = {}
    elem['id'] = id
    elem['temperature'] = (random.randint(500,689)/10, random.randint(690,829)/10)[random.randint(0,999) > 300]
    (random.randint(500,689)/10, random.randint(690,889)/10)[random.randint(0,999) > 300]
    elem['mileage'] = (random.randint(1000,1999), random.randint(2000,5000))[random.randint(0,999) > 300]
    elem['subscription'] = ('Customer', 'Subscriber')[random.randint(0,999) > 100]
    elem['humidity'] = (random.randint(100,499)/10, random.randint(500,999)/10)[random.randint(0,999) > 600]
    data += [elem]

pd.DataFrame(data=data).to_csv('BIKE.csv', sep=';', encoding='utf-8', index=False)
