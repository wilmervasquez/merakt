ventas = [
  {'titulo': 'Don Quijote', 'autor': 'Cervantes', 'precio': 15.99},
  {'titulo': 'Cien años de soledad', 'autor': 'García Márquez', 'precio': 12.99}, 
  {'titulo': 'El principito', 'autor': 'Saint-Exupéry', 'precio': 9.99},
  {'titulo': 'Cien años de soledad', 'autor': 'García Márquez', 'precio': 12.99},
  {'titulo': 'El Quijote', 'autor': 'Cervantes', 'precio': 15.99}, 
  {'titulo': 'El principito', 'autor': 'Saint-Exupéry', 'precio': 9.99},
  {'titulo': 'Rayuela', 'autor': 'Cortázar', 'precio': 14.99},
  {'titulo': 'El Quijote', 'autor': 'Cervantes', 'precio': 15.99},
  {'titulo': 'Rayuela', 'autor': 'Cortázar', 'precio': 14.99}
]

# 📌 Tareas
# ✅ 1. Ordena los libros por cantidad de ventas de mayor a menor.
libros = {}

for libro in ventas:
  titulo = libro['titulo']
  if titulo in libros:
    libros[titulo] += 1
  else:
    libros[titulo] = 1

libros = map(lambda lib: {'libro':lib[0], 'ventas': lib[1]}, list(libros.items()))
libros = sorted(libros, key = lambda lib: lib['ventas'], reverse=True)
print(libros)

# ✅ 2. Calcula el total de ventas de la semana.
precio_total_de_ventas = 0.00
for libro in ventas:
  precio_total_de_ventas += libro['precio']

print(f'💲 Total de ventas de la semana: S/ {precio_total_de_ventas:.2f}')

# ✅ 3. Encuentra el libro más vendido.
libro_mas_vendido = max(libros, key = lambda lib: lib['ventas'] )
print(libro_mas_vendido)

# ✅ 4. Calcula el promedio de precio de los libros vendidos.
promedio = precio_total_de_ventas / len(ventas)
print(f'Promedio de precio de los libros vendidos: {promedio:.2f}')

# ✅ 5. Crea una lista de todos los autores únicos.
autores = []
for libro in ventas:
  if not(libro['autor'] in autores):
    autores.append(libro['autor'])

print(f"Autores: {autores}")

# ✅ 6. Encuentra el libro más caro y el más barato vendidos.
libro_mas_caro = max(ventas, key = lambda libro: libro['precio'])
libro_mas_barato = min(ventas, key = lambda libro: libro['precio'])

print(f"El libro mas caro es {libro_mas_caro['titulo']} con un precio de {libro_mas_caro['precio']}")
print(f"El libro mas barato es {libro_mas_barato['titulo']} con un precio de {libro_mas_barato['precio']}")