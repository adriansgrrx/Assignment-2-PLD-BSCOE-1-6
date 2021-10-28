appleQuestion = int(input("How many apples do you want to buy?: "))
orangeQuestion = int(input("How many oranges do you want to buy?: "))

applePrice = (20)
orangePrice = (25)

totalApplePrice = appleQuestion * applePrice
totalOrangePrice = orangeQuestion * orangePrice
totalPayablePrice = totalApplePrice + totalOrangePrice

print(f"The total amount is {totalPayablePrice}")