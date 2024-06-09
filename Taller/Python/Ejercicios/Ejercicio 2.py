print("CONSULTA SI YA TE JUBILASTE")

añoDeNacimiento = int(input("Ingrese su año de Nacimiento: "))
añoActual = int(input("Ingrese el año actual: "))

while añoDeNacimiento > añoActual:
  print("◇ ¡El año actual deberia ser mayor a la fecha de nacimiento!")
  añoActual = int(input("Ingrese de nuevo el año actual: "))

edad = añoActual - añoDeNacimiento
print(f"◇ Tienes {edad} años")

if edad >= 65:
  print("¡Felicitacines! Puedes jubilarte este año.")
else:
  print("Aun no cumples con la edad para jubilarte.") 