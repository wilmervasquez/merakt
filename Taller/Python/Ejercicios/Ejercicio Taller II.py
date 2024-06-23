from decimal import Decimal

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
# 1. Ordena los libros por cantidad de ventas de mayor a menor.
ventas_por_titulo = {}
for venta in ventas:
  titulo = venta['titulo']
  if titulo in ventas_por_titulo:
    ventas_por_titulo[titulo] += 1
  else:
    ventas_por_titulo[titulo] = 1

def iod(libro):
  print(f"🧪 {ventas_por_titulo[libro['titulo']]} m")
  return libro['titulo']

ventas_ordenadas = sorted(ventas, key = iod, reverse=True)

for libro in ventas_ordenadas:
  print(f'📌 {libro}')
print(ventas_ordenadas)



# 2. Calcula el total de ventas de la semana.
total_de_ventas = Decimal('0.0')
for libro in ventas:
  total_de_ventas += Decimal(str(libro['precio']))

print(f'Total de ventas: S/ {total_de_ventas}')

# 3. Encuentra el libro más vendido.

# 4. Calcula el promedio de precio de los libros vendidos.
promedio = total_de_ventas / Decimal(str(len(ventas)))
print(f'Promedio: {promedio}')

# 5. Crea una lista de todos los autores únicos.
autores = []
for libro in ventas:
  if not(libro['autor'] in autores):
    autores.append(libro['autor'])

print(autores)

# 6. Encuentra el libro más caro y el más barato vendidos.
libro_mas_caro = dict(ventas[0])
libro_mas_barato = dict(ventas[0])

for libro in ventas:
  if libro['precio'] > libro_mas_caro['precio']:
    libro_mas_caro['titulo'] = libro['titulo']
    libro_mas_caro['autor'] = libro['autor']
    libro_mas_caro['precio'] = libro['precio']

  if libro['precio'] < libro_mas_barato['precio']:
    libro_mas_caro['titulo'] = libro['titulo']
    libro_mas_caro['autor'] = libro['autor']
    libro_mas_caro['precio'] = libro['precio']

print(libro_mas_caro)
print(libro_mas_barato)