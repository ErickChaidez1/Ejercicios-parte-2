import csv
from collections import Counter

Rutas = []
with open('synergy_logistics_database.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0

    for XD in csv_reader:
        if line_count == 0:
            
            line_count += 1
        else:
            aux = str(XD[2]),str(XD[3])
            Rutas.append(aux)
            
            line_count += 1
   
    res = Counter(Rutas)
    sorted(res, reverse=True)

    print(res)
    
    # ¿Cuáles son esas 10 rutas? 

    # ('South Korea', 'Vietnam'): 497, 
    # ('Netherlands', 'Belgium'): 437, 
    # ('USA', 'Netherlands'): 436, 
    # ('Japan', 'Mexico'): 385, 
    # ('China', 'Mexico'): 351, 
    # ('China', 'Japan'): 343, 
    # ('Germany', 'China'): 328, 
    # ('Japan', 'Brazil'): 306, 
    # ('Germany', 'France'): 299, 
    # ('South Korea', 'Japan'): 294

    # ¿Le conviene implementar esa estrategia? ¿Por qué?
    # Si, porque son las que mas venden