#MoRequiem 2015
#The following line will make you insert the cost of your meal, not including taxes.
meal = float(input("-What is the cost of the meal? \n"))

#The tax is set on kenosha restaurant tax, edit if needed; also tip is 15 percent, later will add question for increase or decrease in tip
tax = 0.055
tip = 0.15

#The following two lines will calculate the tax on your meal, and the total with taxes
tax = meal * tax
meal = meal + tax

#The following two lines calculate the tip to give and the subtotal
tip = meal * tip
total = meal + tip

#The following set of lines displays the finished calculations in: total, tip, and subtotal
print ("""-Total: ${0:10.2f}
-Tip: ${1:10.2f}
-Subtotal: ${2:10.2f}""".format(meal, tip, total))

tipOk = input("Is the tip amount (15%) ok? \a")

tipOk.uppercase()

if(tipOk == N):
tip1 = .5
meal1 = meal * tip1
print("5% : ${0:10.2f})"
