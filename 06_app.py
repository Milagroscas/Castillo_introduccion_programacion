# Averiguando los tipos de datos de las variables

# Variable de tipo cadena de texto
dispositivo = "computador"
print(dispositivo)
print(type(dispositivo))

# Variable de numero entero
cantidad = 45
print(cantidad)
print(type(cantidad))

# Variable de tipo decimal / flotante
precio = 14.99
print(precio)
print(type(precio))

# Variable de tipo decimal / flotante
precio = "14.99"
print(precio)
print(type(precio))

# Tipo de dato boleano
# Validar si un cliente es activo
is_active_client = True
print(is_active_client)
print(type(is_active_client))

# Tipo de dato de fecha
# Fecha de cumpleaños
from datetime import date
fecha_cumple = date(1987, 7, 25) # (yyyy, mm,dd)
print(fecha_cumple)
print(f"la fecha de cumpleaños es: {fecha_cumple}")
fecha_formateada = fecha_cumple.strftime("%d%m%y")
print(f"la fecha con formato es: {fecha_formateada}")
print(type(fecha_cumple))
