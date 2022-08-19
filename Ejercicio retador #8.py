
Clientes={45471:["Luis Perez", 45, "BJX" , True], 8944411:["Fernanda Garcia", 25, "JAL", True],
15223:["Alejandra Ortiz", 33, "GDL", True]}
ClientesPreferentes = {45471:["Luis Perez", 45, "BJX" , True], 8944411:["Fernanda Garcia", 25, "JAL", True],
15223:["Alejandra Ortiz", 33, "GDL", True]}



while True:
    SumaEdad = 0
    SumaEdadPreferente = 0
    print("================================")
    print("(1) Añadir nuevos clientes")
    print("(2) Listar todos los clientes")
    print("(3) Listar clientes preferentes")
    print("(4) Eliminar un cliente mediante ID del INE")
    print("(5) Edad promedio de todos los clientes")
    print("(6) Edad promedio de clientes preferentes")
    print("(7) Salir")
    print("================================")
    Opcion = int(input(""))
    if Opcion == 7:
        break
    elif Opcion == 1:
        ID = int(input("Ingrese ID de INE/IFE: "))
        Nombre = input("Ingrese el nombre: ")
        Edad = int(input("Ingrese la edad: "))
        Destino = input("Ingresa IATA de destino: ")
        OpcionPreferente = input("Cliente preferente (Si/No): ")

        if OpcionPreferente == "Si" or OpcionPreferente == "SI" or OpcionPreferente == "si" :
            OpcionPreferente = True
            ClientesPreferentes[ID] = [Nombre, Edad, Destino, OpcionPreferente]

        elif OpcionPreferente == "No" or OpcionPreferente == "NO" or OpcionPreferente == "no":   
            OpcionPreferente = False
 
        Clientes[ID] = [Nombre, Edad, Destino, OpcionPreferente]
          
    elif Opcion == 2:
        ClientesLista = list(Clientes)
        for k in ClientesLista:
            del(Clientes[k][1:4])
        print(Clientes)

    elif Opcion == 3:
        ClientesLista2 = list (ClientesPreferentes)
        for k in ClientesLista2:
            del(ClientesPreferentes[k][1:4])
        print(ClientesPreferentes)

    elif Opcion == 4:
        delete = int(input("Ingrese ID a eliminar: "))
        del(Clientes[delete])
        print(Clientes)

    elif Opcion == 5:
        ClientesLista3 = list(Clientes)
        for S in ClientesLista3:
            SumaEdad+=int((Clientes[S][1]))
        PromedioTotal = SumaEdad / (len(Clientes))
        print(PromedioTotal)
    elif Opcion == 6:
        ClientesLista4 = list(ClientesPreferentes)
        for SP in ClientesLista4:
            SumaEdadPreferente+=int((ClientesPreferentes[SP][1]))
        PromedioPreferente = SumaEdadPreferente / (len(ClientesPreferentes))
        print(PromedioPreferente)

