def bubleSort(lista: list[int]) -> list[int]:
    
    # ingresar los datos a lista 
    while True:

        numero = input("Ingresa un numero 'c' para terminar: ")
        
        if numero == 'c':
            break
        elif numero:
            if numero.isalpha():
                print('no es numero intenta poner nuevamente un valor numerico')
            # elif numero.isspace():
            #     print(f'has ingresado un {numero} ingresa un numero')
            elif numero == ' ':
                print('has agregado un espacio')
            else:
                print(numero)
                lista.append(int(numero))
        else:
            print('no has ingresado ningun caracter')

    #saber cuantos elementos hay en la lista
    numElementos = len(lista)

    #volver a iniciar el ordenamiento: tantas veces como numeros hay en la lista
    for paso in range (numElementos - 1):

        #recorrer la lista
        for index in range(numElementos - 1 - paso):
            #obtener el valor actual y el valor siguiente
            #si el valor actual es mayor que el valor siguiente: hacer un cambio entre los dos
            if lista[index] > lista[index+1]:
                contenedor = lista[index]
                lista[index] = lista[index+1]
                lista[index+1] = contenedor

    # verificar que no sean letras

    
        # lista = []

        # while numero != 'c':
                
        #     numero.append = input("ingrese un numero")
        #     if numero != 'c':
        #         break
    return lista



print(bubleSort([]))