# ✅ TAREA: Sistema de Gestion de Inventario
# ✏️ Implementa las clases Producto e Inventario con los atributos y metodos descritos
# ⭐ Clase: Producto
class Producto:
  def __init__(self, nombre, codigo, precio, stock):
    self.nombre = nombre
    self.codigo = codigo
    self.precio = precio
    self.stock = stock

  def actualizar_stock(self, cantidad):
    self.stock = cantidad

  def aplicar_descuento(self, porcentaje):
    descuento = self.precio * (porcentaje / 100) 
    return self.precio - descuento
  
# ⭐ Clase: Inventario
class Inventario:
  def __init__(self, products = []):
    self.lista_de_productos = products

  def agregar_producto(self, product):
    self.lista_de_productos.append(product)

  def buscar_producto(self, codigo):
    for producto in self.lista_de_productos:
      if producto.codigo == codigo:
        return producto

  # ✏️ En el método vender_producto(), asegúrate de actualizar el stock y manejar el caso de stock insuficiente
  def vender_producto(self, codigo, cantidad, descuento = 0):
    product = self.buscar_producto(codigo)
    if product != None:
      if product.stock >= cantidad:
        precio_total = product.aplicar_descuento(descuento) * cantidad
        product.actualizar_stock(product.stock - cantidad)
        return f"Total de importe S/ {precio_total}"
      else: return 'No hay suficiente cantidad de productos'
    else: return 'El producto con codigo {codigo} no existe para vender'

  # ✏️ El método reporte_stock debe mostrar una lista de todo los productos con su cantidad actual
  def reporte_stock(self, tabla = False):
    if tabla:
      print("------ PRODUCTOS DISPONIBLES --------")
      print("Producto       Codigo    Precio      Stock")
      lista_de_productos = sorted(self.lista_de_productos, key = lambda product: product.stock)
      for product in lista_de_productos:
        nombre, codigo, precio, stock = product.nombre, product.codigo,  product.precio, product.stock
        print(f"◇ {nombre:<12} {codigo:<8} 💸 {precio:<6.2f} {stock:>5} uds.")
      print("-------------------------------------")

    return list(map(lambda product: product.__dict__, self.lista_de_productos ))
   
    

  # ✏️ Añade un método en Inventario para calcular el valor total del inventario 
  def calcular_el_valor_total(self):
    info = { 
      'cantidad_de_productos': len( self.lista_de_productos ), 
      'precio_total': 0, 
      'cantidad_de_productos_por_unidad': 0
    }

    for producto in self.lista_de_productos:
      info['precio_total'] += producto.precio * producto.stock
      info['cantidad_de_productos_por_unidad'] += producto.stock

    return info

# 📌 Definiendo algunos productos
products = [
  Producto("Camisa", "032", precio = 15.00, stock = 30),
  Producto("Zapato", "123", precio = 50.00, stock = 20),
  Producto("Sombrero", "845", precio = 25.20, stock = 15),
  Producto("Chaqueta", "234", precio = 99.90, stock = 5),
  Producto("Bufanda", "890", precio = 10.00, stock = 50),
  Producto("Guante", "345", precio = 20.00, stock = 40),
]

# 📌 Creando un inventario y añadiendo los productos
store = Inventario(products)

store.vender_producto('XYZ', 12)
store.reporte_stock(True)

print(store.calcular_el_valor_total())