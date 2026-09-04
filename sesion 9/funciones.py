#Registrar las edades que tioene n cantidad de personas y mostrar y mostrar la edad mas alta y mas baja y la cantidad de personas registradas.
ages = []

def addAge(age):
    ages.append(age)

def getMaxAge():
    maxAge = ages[0]
    for age in ages:
        if age > maxAge:
            maxAge = age
    return maxAge

def getMinAge():
    minAge = ages[0]
    for age in ages:
        if age < minAge:
            minAge = age
    return minAge

def showSize():
    return len(ages)

def showAges():
    return ages

while True:
    try:
        age = int(input("Que edad tenes mae? "))
        if age > 3:
            addAge(age)
        else:
            print("Es imposible que un estudiante tenga esa edad xd")

        answer = input("Ingresa otro [S/N]: ")
        if answer.upper() != "S":
            break

    except ValueError:
        print("Men, un numero entero pls")

print("Mostrar edades")
print (f"La cantidad de edades registradas es: {showSize()}")
print(showAges())
print (f"El mas mayor es: {getMaxAge()}")
print (f"El mas menor es : {getMinAge()}")