#MoReqquiem 2015
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
print ("""
-Total: {0:10.2f} $
-Tip: {1:10.2f} $
-Subtotal: {2:10.2f} $
""".format(meal, tip, total))



tip_ok = float(input("""Is the tip amount (15%) ok?
insert 0 for "NO" and  any other for "YES" \n"""))

if (tip_ok == 0):
    tip1 = .05
    meal1 = meal * tip1
    print("""
1:   -5% : {0:10.2f} $""".format(meal1))
    
    tip2 = .08
    meal2 = meal * tip2
    print("2:   -8% : {0:10.2f} $".format(meal2))
    
    tip3 = .10
    meal3 = meal * tip3
    print("3:   -10% : {0:10.2f} $".format(meal3))
    
    tip4 = .20
    meal4 = meal * tip4
    print("4:   -20% : {0:10.2f} $".format(meal4))
    
    tip_ch = "tip" + str(input("""please select one 
insert 0 for end program \n"""))
    
    if tip_ch == "tip1":
        tip_ch = tip1
    if tip_ch == "tip2":
        tip_ch = tip2
    if tip_ch == "tip3":
        tip_ch = tip3
    if tip_ch == "tip4":
        tip_ch = tip4

    u_tip = meal * tip_ch
    
    su_total = meal + u_tip
    print ("""
-Total: {0:10.2f} $
-Tip: {1:10.2f} $
-Subtotal: {2:10.2f} $
""".format(meal, u_tip, su_total))


else:
    print ("""
    Thanks for using mealCalculator, remember to tip nicely!""")
