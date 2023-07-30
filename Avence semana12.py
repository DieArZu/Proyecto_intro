import os
os.system("cls")
#print(" Proyecto Intro a la Progra: Sistema Tienda Pequeña ".center(60,'*'))
print("")
intentosusuario=[]
intentosclave=[]
intentos=1
#Carga del invenetario inicial 
nombre={
    "pam1" : "Pantalon 1" ,
    "pam2" : "Pantalon 2",
    "pam3" : "Pantalon 3",
    "cam1" : "Camisa 1",
    "cam2" : "Camisa 2",
    "cam3" : "Camisa 3",
    "pat1" : "Pantaloneta 1",
    "pat2" : "Pantaloneta 2",
    "pat3" : "Pantaloneta 3"
}
cantidad={
    "pam1" : 10 ,
    "pam2" : 30,
    "pam3" : 22,
    "cam1" : 55,
    "cam2" : 42,
    "cam3" : 14,
    "pat1" : 44,
    "pat2" : 36,
    "pat3" : 10
}
color={
    "pam1" : "Azul" ,
    "pam2" : "Negro",
    "pam3" : "Verde",
    "cam1" : "Azul",
    "cam2" : "Negro",
    "cam3" : "Verde",
    "pat1" : "Azul",
    "pat2" : "Negro",
    "pat3" : "Verde"
}
talla = {
    "pam1" : "S" ,
    "pam2" : "M",
    "pam3" : "L",
    "cam1" : "S",
    "cam2" : "M",
    "cam3" : "L",
    "pat1" : "S",
    "pat2" : "M",
    "pat3" : "L"
}
precio={
    "pam1" : 5000 ,
    "pam2" : 6000,
    "pam3" : 8000,
    "cam1" : 3000,
    "cam2" : 6000,
    "cam3" : 7000,
    "pat1" : 3000,
    "pat2" : 4500,
    "pat3" : 5650
}

while intentos<=3:
    #os.system("cls")
    print(" Proyecto Intro a la Progra: Sistema Tienda Pequeña ".center(60,'*'))
    print("")
    usuarios = {'David' : 'proyecto','Diego' : '123'}
    print("Intento de acceso", intentos)
    nuevouser =str(input('Ingrese su nombre de usuario: '))
    nuevacontr = str(input('Ingrese su contraseña: '))
    intentosusuario.append(nuevouser)
    intentosclave.append(nuevacontr)
    if nuevouser in usuarios and usuarios[nuevouser] == nuevacontr:
        os.system("cls")
        print("Inicio de sesión exitoso")
        print("")
        Menu1=1
        while Menu1>=1:
            print(" MENU ".center(60,"*"))
            print('(1) Registrar nuevo usuario'.center(60,'-'))
            print('(2) Revisar 1 producto'.center(60,'-'))
            print('(3) Ver inventario'.center(60,'-'))
            print('(4) Ingresar nuevo producto'.center(60,'-'))
            print('(5) Crear factura'.center(60,'-'))
            print('(6) Salir'.center(60,'-'))
            Menu1= (input('Ingrese su opcion a elejir: '))
                
            if Menu1.isdigit()==True:
                Menu1=float(Menu1)
                if Menu1==1:
                    print("")
                    nuevouser =str(input('Ingrese su nombre de usuario: '))
                    nuevacontr = str(input('Ingrese la contraseña: '))
                    if nuevouser in usuarios:
                        print('ERROR ya existe ese usuario por favor inicie sesion de nuevo')
                        #print("Saliendo".center(60,'-'))
                    else:
                        usuarios[ nuevouser ] = nuevacontr
                        print('Creado con exito.')
                                        

                elif Menu1==2:
                 print("")
                 print("\nLista de Codigos\n")
                 #print("pam1-> Pantalon1\npam2-> Pantalon2\npam3-> Pantalon3\ncam1-> Camisa1\ncam2-> Camisa2\ncam3-> Camisa3\npat1-> Pantaloneta1\npat2-> Pantaloneta2\npat3-> Pantaloneta3\n")
                 for k,v in nombre.items():
                    print("Cod: {0} para --> {1} ".format(k,v))
                 cod=input("\nDigite el codigo a revisar: ")
                 print(cod)
                 print(nombre[cod].center(60,'-'))
                 print("La cantidad es: ",cantidad[cod])
                 print("El color es: ",color[cod])
                 print("La talla es: ",talla[cod])
                 print("El precio es: ",precio[cod])
                 print("")   
        
                elif Menu1==3:
                    print("")
                    for v in nombre:
                        print( v ," hay ", cantidad[v], " de ", nombre[v])
              

                elif Menu1==4:
                    print("")
                    print("Ingresar nuevo producto".center(60,"-"))
                    codnue=input("Ingrese el nuevo codigo: ")
                    nomnue=input("Ingrese el nombre: ")
                    cantnue=int(input("Ingrese la cantidad inicial: "))
                    colornue=input("Ingrese el color: ")
                    tallanue=input("Ingrese la talla: ")
                    precionue=int(input("Ingrese el precio: "))
                    nombre[codnue]=nomnue
                    cantidad[codnue]=cantnue
                    color[codnue]=colornue
                    talla[codnue]=tallanue
                    precio[codnue]=precionue
                    print("ingreso con exito")
     
                                        
                elif Menu1>6:
                    print("Opcion incorrecta, intente de nuevo")
                    print("")
                        
                elif Menu1==6:
                    print("XXX  SALIR  XXX".center(60,"-"))
                    print("")
                    intentos=0
                    os.system("cls")
                    break
                # FActura
                
                elif Menu1==5:
                    print("")
                    print("Factura".center(60,"-"))
                    nomfac=input("Nombre del cliente: ")
                    faccod=input("Ingrese el codigo: ")
                    faccant=int(input("Ingrese la cantidad vendida: "))
                    if faccod in nombre: 
                        if faccant<= cantidad[faccod]:
                            cantidad[faccod]=cantidad[faccod]-faccant
                            print("Cliente: ",nomfac)
                            print(faccant," ",nombre[faccod]," "," precio: ",precio[faccod]," precio total: ",precio[faccod]*faccant)
                            print("IVA: ",precio[faccod]*faccant*0.13)
                            print("Total: ",precio[faccod]*faccant*0.13+precio[faccod]*faccant)

                                  
                    else:
                        print("Codigo erroneo")











            
            

            else:
                    print("Error digite una opcion, no letras ")
                    Menu1=1
                                         

    else:
        print("XXXX Datos de acceso incorrectos XXXX")
        print("")

   
    intentos=intentos+1 
else:
   print("")
   print("Supero la cantidad de intentos")
   print("XXXXX  Cuenta bloqueda   XXXXX")
   print("")

    
