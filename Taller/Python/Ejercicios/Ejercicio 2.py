yearOfBirth = int(input("Ingrese su año de Nacimiento: "))
yearCurrent = int(input("Ingrese el año actual: "))

age = yearCurrent - yearOfBirth
print(f"- Tu edad es {age}")
if age >= 65:
  print("¡Felicitacines! puedes jubilarte este año.")
else:
  print("Aun no cumles con la edad para jubilarte")