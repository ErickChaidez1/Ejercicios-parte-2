Pasajeros = []
DetallesDeVuelo = []
Informacion = ()
DetallesPromedio = []


Vuelos = ["BJX", "GDL", "JAL"]
PBJX = 0
PGDL = 0
PJAL = 0

SumaBJX = 0
SumaGDL = 0
SumaJAL = 0

PromedioBJX = 0
PromedioJAL = 0
PromedioGDL = 0

while True :
    Nombre = input("Ingresa tu nombre: ")
    if Nombre == 'X' or Nombre == 'x' :
        break
    Edad = int(input("Ingresa tu edad: "))
    Destino = input("Ingresa IATA de destino: ")
    Informacion = (Nombre, Edad, Destino)
    Pasajeros.append(Informacion)
    
    if Destino ==  Vuelos[0] :
        SumaBJX += Edad
    elif Destino == Vuelos[1] :
        SumaGDL += Edad
    elif Destino == Vuelos[2] :
        SumaJAL += Edad
    
for i in range(len(Pasajeros)) :

    if Pasajeros[i][2] == Vuelos[0]:
        PBJX += 1
    elif Pasajeros[i][2] == Vuelos[1]:
        PGDL += 1
    elif Pasajeros[i][2] == Vuelos[2]:
        PJAL += 1


if PBJX > 0 :
    PromedioBJX = SumaBJX / PBJX
    PromedioTuplaBJX = (Vuelos[0], PromedioBJX)
    DetallesTuplaBJX = (Vuelos[0], PBJX)

    DetallesPromedio.append(PromedioTuplaBJX)
    DetallesDeVuelo.append(DetallesTuplaBJX)

if PGDL > 0 :
    PromedioGDL = SumaGDL / PGDL
    PromedioTuplaGDL = (Vuelos[1], PromedioGDL)
    DetallesTuplaGDL = (Vuelos[1], PGDL)

    DetallesPromedio.append(PromedioTuplaGDL)
    DetallesDeVuelo.append(DetallesTuplaGDL)
    

if PJAL > 0 :
    PromedioJAL = SumaJAL / PJAL
    DetallesTuplaJAL = (Vuelos[2], PJAL)
    PromedioTuplaJAL = (Vuelos[2], PromedioJAL)

    DetallesPromedio.append(PromedioTuplaJAL)
    DetallesDeVuelo.append(DetallesTuplaJAL)
print("=================================================")
print("Detalles de vuelos: ")
DetallesDeVuelo.sort(key= lambda x: x[1], reverse = True)
print(DetallesDeVuelo)

print("Edad promedio por vuelo: ")
print(DetallesPromedio)