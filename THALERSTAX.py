#The Land of Milk and Honey - HAPPINESS
aIncome = float(input("Enter annual income: "))

#surplus calculations stored
if aIncome >= float(85528):
    surplus = aIncome - 85528


#evaluations: thalers
#happiness limit evaluations
#the "so-called tax relief"
if aIncome < float(85528):
    tax = round((.18 * aIncome) - 556.02, 2)


elif aIncome >= float(85528):
    tax = round(14839.02 + surplus, 2)


# Write your code here.
#Edube wrote this line I don't like it: tax = round(tax, 0)
print("The tax is:", tax, "thalers")



survey=input("Do you know what you paid for? Y/N\n")

if survey == "N":
    print('Happiness reduction applied')
elif survey == "Y":
    print('May the odds be ever in your favor')
else:
    print("Error. The tax application is having a crisis. Probably like you. Retry if  you have enough willpower. Thank you.")


print("Congratulations! Your happiness has been limited accordingly.")

























