# Regex para obtener numeros telefonicos - Scraper

# Teoria:
'''
Las expressiónes regulares son una forma de expresar una serie de patrones ya sea para buscar o reemplazar, En este ejemplo se muestra una forma de validar y buscar numeros telefonicos.
'''
# Regex manual:
def numero_telefonico(texto): #415-555-1212
    if len(texto) != 12:
        return False # El tamaño del numero telefonico no es correcto
    for i in range(0,3):
        if not texto[i].isdecimal():
            return False # No contiene codigo de area
    if texto[3] != '-':
        return False # No contiene guion
    for i in range(4,7):
        if not texto[i].isdecimal():
            return False # No contiene los 3 primeros numeros
    if texto[7] != '-':
        return False # No contiene guion
    for i in range(8,12):
        if not texto[i].isdecimal():
            return False # No contiene los 4 ultimos numeros
    return True

# Verificamos el numero con la funcion
print(numero_telefonico('415-555-1212'))

# Mensaje de prueba
mensaje = 'Hola, mi nombre es Juan y mi numero es 415-555-1212, cualquier duda que tenga tambien puede enviarme un mensaje a: 415-555-9999'

# Scraper manual:

numero_encontrado = False

for i in range(len(mensaje)):

    fragmento = mensaje[i:i+12] # Tomamos el fragmento de 12 caracteres, que le pasaremos a la funcion
    
    if numero_telefonico(fragmento):
        print('Numero encontrado: ' + fragmento)
        numero_encontrado = True
if not numero_encontrado:
    print('No se encontro ningun numero telefonico')