yourMoney = int(input("Enter the amount of money you have: "))
applePrice = int(input("How much for an apple?: "))

maxApples = yourMoney // applePrice
yourChange = (yourMoney - maxApples * applePrice)

print(f"You can buy {maxApples} apples and your change is {yourChange} pesos")