# 6. Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo rectángulo como el de más abajo, de altura el número introducido.

#numero = int (input ("Escribe un numero: "))

#for i in range(0, numero+1):
#    print (i*("*"))

# 5. Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.

#cantidad_invertir = float (input("Cantidad a invertir: "))
#interes_anual = float(input ("interes anual: "))
#numero_años = int (input ("numero de años: "))

#interes_anual_1= (1 + interes_anual/100)

#for años in range (1, numero_años+1):
 #   print (cantidad_invertir * interes_anual_1**(años))


# 
#7. numero = int (input("Escrieb un nuemro: "))

#for i in range (1, 11):
 #   multiplicacion =  numero * i 
  #  print (i,  " * ", numero, "= ", multiplicacion)

#8 Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.


contador = 0 
while True:
    contraseña = input ("Escribe una contraseña: ")
    if contraseña =="Holamundo": 
        print ("Contraseña es correcta")
        contador = contador + 1
        
    