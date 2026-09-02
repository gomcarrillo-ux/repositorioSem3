#Sumar dos numeros y mostrar el resultado
#Parametro es la variable que se define cuando se crea la funcion
def getsum (number1, number2):
    return number1 + number2

def showresult (message, result):
    return f"{message} {result}"

print ("Dime un numero: ")
num1 = float(input())
print ("Dime otro numero: ")
num2 = float(input())
#Argumento es el valor que se envia a la funcion cuando se llama
sum = getsum(num1, num2)
print (showresult("El resultado de la suma es: ", sum))