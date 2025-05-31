# Actividad 1
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# Actividad 2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# Actividad 3
lista_frutas = list(precios_frutas.keys())
print("Frutas:", lista_frutas)

# Actividad 4
agenda = {}
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    numero = input(f"Ingresá el número de {nombre}: ")
    agenda[nombre] = numero

consulta = input("Ingresá el nombre del contacto que querés consultar: ")
if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print("Ese contacto no existe.")

# Actividad 5
frase = input("Ingresá una frase: ")
palabras = frase.lower().split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

conteo_palabras = {}
for palabra in palabras:
    conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1
print("Conteo de palabras:", conteo_palabras)

# Actividad 6
alumnos = {}
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i+1}: ")
    notas = []
    for j in range(3):
        nota = float(input(f"Ingresá la nota {j+1} de {nombre}: "))
        notas.append(nota)
    alumnos[nombre] = tuple(notas)

for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre} tiene un promedio de {promedio:.2f}")

# Actividad 7
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos parciales:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

# Actividad 8
stock = {
    'leche': 10,
    'pan': 20,
    'huevos': 30
}

producto = input("Ingresá el nombre del producto que querés consultar o actualizar: ").lower()
if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    agregar = int(input("¿Cuántas unidades querés agregar?: "))
    stock[producto] += agregar
    print(f"Nuevo stock de {producto}: {stock[producto]}")
else:
    nuevo_stock = int(input(f"{producto} no existe. Ingresá el stock inicial: "))
    stock[producto] = nuevo_stock
    print(f"{producto} agregado con stock de {nuevo_stock}")

# Actividad 9
agenda_eventos = {
    ('Lunes', '10:00'): 'Reunión de equipo',
    ('Martes', '14:00'): 'Clase de inglés',
    ('Viernes', '18:00'): 'Gimnasio'
}

dia = input("Ingresá el día: ")
hora = input("Ingresá la hora (hh:mm): ")
evento = agenda_eventos.get((dia, hora), "No hay actividad registrada en ese horario.")
print("Actividad:", evento)

# Actividad 10
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago',
    'Paraguay': 'Asunción'
}

capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print("Diccionario invertido:", capitales_paises)
