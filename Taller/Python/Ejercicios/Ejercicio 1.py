print("CONSULTA SI UN AÑO ES BISIESTO")

año = int(input("Ingrese un año: "))

if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
  print(f"El año {año} es un año bisiesto")
else: 
  print(f"El año {año} no es un año bisiesto")
