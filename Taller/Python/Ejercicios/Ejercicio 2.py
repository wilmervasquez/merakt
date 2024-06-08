añoDeNacimiento = int(input("Ingrese su año de Nacimiento: "))
añoActual = int(input("Ingrese el año actual: "))

edad = añoActual - añoDeNacimiento
print(f"- Tu edad es {edad}")

if edad >= 65:
  print("¡Felicitacines! puedes jubilarte este año.")
else:
  print("Aun no cumles con la edad para jubilarte") 