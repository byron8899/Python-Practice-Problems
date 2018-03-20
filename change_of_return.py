# Change Return Program - The user enters a cost and then the amount of money 
# given. The program will figure out the change and the number of quarters, 
# dimes, nickels, pennies needed for the change.

getChange = 0

quarter = 0
dime = 0
nickel = 0
penny = 0

def countQuarters():
    global getChange, quarter 
    while(0.25 <= getChange):
        getChange = getChange - 0.25
        quarter += 1
def countDimes():
    global getChange, dime 
    while(0.10 <= getChange):
        getChange = getChange - 0.10
        dime += 1
        
def countNickels():
    global getChange, nickel 
    while(0.05 <= getChange):
        getChange = getChange - 0.05
        nickel += 1  

def countPennies():
    global getChange, penny
    while(0.01 <= getChange):
        getChange = getChange - 0.01
        penny += 1  
    

inputMoney = 0

inputCost = float(input('Enter the cost: '))
print('You entered ${}.'.format(inputCost))
print('')

inputMoney = float(input('Enter the money you what to pay: '))
print('You entered ${}.'.format(inputMoney))
print('')
getChange = inputMoney - inputCost
print('''Your change is ${:.2f}'''.format(getChange))

countQuarters()
countDimes()
countNickels()
countPennies()

print('Quarters: {}, Dimes: {}, Nickels: {}, Pennies: {}'.format(quarter,
            dime, nickel, penny))


