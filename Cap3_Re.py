import re # Libreria para expresiones regulares (RegEx) (10/10)

mensaje = 'Hola, mi nombre es Juan y mi numero es 415-555-1212, cualquier duda que tenga tambien puede enviarme un mensaje a: 415-555-9999'

numero_telefonico_regex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # Creamos una expresion regular

coincidencias = numero_telefonico_regex.findall(mensaje) # Buscamos los numeros telefonicos en el mensaje

for i in range(len(coincidencias)): # Recorremos los numeros encontrados
    print('Numero encontrado: ' + coincidencias[i])