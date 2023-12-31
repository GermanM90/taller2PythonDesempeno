import random
# Diccionario Departamento con Llave y Capital
Departamentos = {
    "Amazonas": "Leticia", "Antioquia": "Medellin", "Arauca": "Arauca", "Atlantico": "Barranquilla",
    "Bogota": "Bogota", "Bolivar": "Cartagena", "Boyaca": "Tunja", "Caldas": "Manizales"}
# Ciclo FOR para imprimir departamento y Capital
for x, y in Departamentos.items():
    print('Departamento:', x, '-- Capital: ', y)
# DEPARTAMENTOS.keys convierte mi arreglo a una lista y muestra solo las llaves del dic
DepartamentosaListas = Departamentos.keys()
# RANDON.CHOISE() choise saca 1 departamento aleatorio de la lista recien creada
DepartamentoAleatorio = random.choice(list(DepartamentosaListas))
capital = Departamentos[DepartamentoAleatorio]
# Genero la pregunta concatenando la variable DepartamentosAleatorio
print('Cual es la capital del Departamento de: ', DepartamentoAleatorio, '?')
# la variable CAPITAL se comparará con RESPUESTA usando IF y ciclo While + contador
contador = 0
while contador < 3:
    contador += 1
    respuesta = input('Respuesta:  ').capitalize()
    if respuesta == 'salir':
        print('Gracias por participar, hasta pronto!')
        break
    if respuesta == capital:
        print("Felicitaciones, es correcto!!!!!")
        break
    else:
        print("Estas equivocado, intentalo nuevamente")
    if contador == 3:
        print('¡HASTA LUEGO! ... Intentos máximos superados (3)')