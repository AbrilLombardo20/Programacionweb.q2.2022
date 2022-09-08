#EJERCICIO 1 TIPO PARCIAL
#cuantos packs se compran de cada uno
#facturación total
#promedio de facturación para compras
#Cargos extra servicios
"""montoservicio=0
#packs
packlimpieza= 0
packalmacen=0
packfrescos=0
packlibreria=0
#facturaciontotal
facturacion=0
#facturacion compras dentro de 48 hs
montofacturacion=0
cantvecesfacturacion=0
#facturaciones
factura1=0
factura2=0
factura3=0
factura4=0
promedio72hs=0
servicios=0

while(True):
    print("Ingresar los siguientes datos: ")
    direccion=input("Ingrese su dirección: ")
    print("1. PACK LIMPIEZA")
    print("2. PACK ALMACEN")
    print("3. PACK FRESCOS")
    print("4. PACK LIBRERIA")
    pack=int(input("Introduce el numero del pack que desee: "))
    if pack==1:
        packlimpieza+=1
        facturacion+=900
    elif pack==2:
        packalmacen+=1
        facturacion+=800
    elif pack==3:
        packfrescos+=1
        facturacion+=1200
    elif pack==4:
        packlibreria+=1
        facturacion+=1000
    else:
        pack=int(input("Introduzca un pack válido: "))
    cantidad=int(input("Introduce la cantidad de packs que desee: (debe ser menor que 4"))
    while cantidad>4 or cantidad<1:
        cantidad=int(input("Introduzca una cantidad menor a 4: "))
    if cantidad==1:
        facturacion*=1
    elif cantidad==2:
        facturacion*=2
    elif facturacion==3:
        facturacion*=3
    elif facturacion==4:
        facturacion*=4
    print( "1. entrega en 24 horas")
    print("2. Entrega en 48 horas")
    print("3. Entrega en 72 horas")
    servicio=int(input("Introduzca el numero de servicio que desee: "))
    while servicio!=1 and servicio!=2 and servicio !=3:
        servicio=int(input("Introduzca un servicio válido: "))
    if servicio==1:
        montoservicio+=200
        servicios+=1
    elif servicio==2:
        montoservicio+=150
        servicios+=1
    elif servicio==3:
        montoservicio+=50
        promedio72hs+=1
        servicios+=1
    continuar=input("DESEA CONTINUAR? De no ser así coloque FIN ")
    if continuar=="FIN":
        break
    print("La cantidad comprada de packs de limpieza es de: ", packlimpieza, "de packs de almacen: ", packalmacen, "de packs frescos: ", packfrescos, "de packs de libreria: ", packlibreria)
    print("La facturación total es de: ", facturacion)
    print("El promedio de facturacion para compras de 72 hs es de: ", servicios*100//promedio72hs)
"""

#EJERCICIO 2 INTEGRADOR
#Generar 10 pares de numeros aleatorios
import random
from random import randint
numprimopares=0
numpares=0
segundomultiplo=0
prompares=0
max=10
contador=0
while(contador<max):
    numero=random.randint(-20, 20)
    numero2=random.randint(-20, 20)
    print(numero, numero2)
    if numero+numero2>1 and (numero+numero2)%2==0:
        numprimopares+=1
    if numero%2==0:
        numpares+=1
        prompares+=numero
    if numero2%2==0:
        numpares+=1
        prompares+=numero2
    if numero2%numero==0:
        segundomultiplo+=1
    contador+=1
print("La cantidad de veces que el par sumo un numero par es: ", numprimopares)
print("El promedio entre los numeros pares es de: ", prompares//numpares)
print("El porcentaje donde el segundo número es múltiplo del primero es de: ", (segundomultiplo*100)//100)

        

    
