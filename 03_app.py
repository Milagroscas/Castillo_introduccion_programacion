# "Variables

# Las variables son palabras específicas que utilizamos para asignar y almacenar valores específicos que podemos recuperar en cualquier momento.

# Variable nombre
nombre = "Jesús"
telefono = 997654111
name = "Alberto"

# Visualizando el contenido de las variables
print(nombre)
print(telefono)
print(name)

# Jugando con variables
age = 30
print(age)
print(f"edad: {age}")

district = "San luis"
print(district)
print(f"nombre de Distrito: {district}")

# Precio de un producto
price = 45.99
print(price)
print(f"El precio es {price}")

# Es un cliente activo
is_active_client = True
print(is_active_client)
print(f"¿Esta activo? {is_active_client}")

# Trabajando con fechas
from datetime import date
fecha_clase = date(1987, 7, 25) # (yyyy, mm,dd)
print(fecha_clase)
print(f"la fecha de hoy es: {fecha_clase}")

fecha_formateada = fecha_clase.strftime("%d%m%y")
print(f"la fecha con formato es: {fecha_formateada}")



 