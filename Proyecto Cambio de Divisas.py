# Proyecto: Cambio de Divisas

from datetime import datetime
usuario = "usuario"
fecha = datetime.today()
HoraMinuto = datetime.today().strftime('%H:%M')


if HoraMinuto < "11:59":
    DiaTardeNoche = "Buenos dias"
if HoraMinuto > "11:59" and HoraMinuto < "19:59":
    DiaTardeNoche = "Buenas tardes"
if HoraMinuto > "19:59":
    DiaTardeNoche = "Buenas noches"


bienvenida = DiaTardeNoche + " estimado " + usuario

dolares = 210

euros_a_recibir = dolares * 0.88

billetes_10 = euros_a_recibir // 10

billetes_1 = (euros_a_recibir - (billetes_10 * 10)) // 1

monedas = euros_a_recibir % 1


print(bienvenida)
print("La tasa de cambio al dia de hoy es de 0.88")
print("1 Dólar estadounidense Es igual a 0.88 Euro")
print("Recibire " + str(dolares) + " dolares")
print("Entregare " + str(euros_a_recibir) + " euros en total")
print("Detalle de billetes y monedas que le serán entregados")
print("Billetes de 10 euros = " + str(billetes_10))
print("Billetes de 1 euro = " + str(billetes_1))
print("Monedas = " + str(monedas))
print("Gracias por tu preferencia !vuelve pronto!")

