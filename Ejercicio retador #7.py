ClientesPreferentes = {}
Clientes = {}

while True:
    print("================================")
    print("(1) Añadir cliente")
    print("(2) Listar todos los clientes")
    print("(3) Listar clientes preferentes")
    print("(4) Salir")
    print("================================")
    Opcion = int(input(""))
    if Opcion == 4:
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
        key = list(Clientes)
        for k in key:
            del(Clientes[k][1:4])
        print(Clientes)

    elif Opcion == 3:
        keys = list (ClientesPreferentes)
        for k in keys:
            del(ClientesPreferentes[k][1:4])
        print(ClientesPreferentes)

