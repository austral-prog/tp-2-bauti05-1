def change():
    expense = 23.75
    money = 100
    print("Ingresar gasto:")
    print(expense)
    print("Dinero recibido")
    print(money)
    print("\nVuelto")
    print("\nPesos:")
    vuelto=(money-expense)
    print(int(vuelto))
    print("Centavos:")
    print(round((vuelto-int(vuelto))*100))

change()
