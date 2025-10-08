temperatura = float(input("ingrese temperatura: "))
escala = input("farenheit(f) o es celsius (c)?")
if escala == "f":
    celsius = (temperatura - 32) * 5/9
    print(celsius)


elif escala == "c":
    farenheit = temperatura *1.8 + 32
    print(arenheit)





else:
    print("escala incorrecta")
    







