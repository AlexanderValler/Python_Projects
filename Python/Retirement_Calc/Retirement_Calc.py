#File Name: Retirement Calculator 
#Author: Alexander Valler 
#Section: D 
#Description: A retirement calculator to manage and return investment amounts and income to find out how many years and at what amount put away, to fing out what amount you retire with
############################################################################################################################### Part 1

m_income = int(input("Enter your pre-retirement final monthly income: "))
m_withdraw = (m_income * .85)   # is going to be 85% of your final monthly income
print("You will need to draw ${0:,.2f} every month from your investments to achieve your goal".format (m_withdraw))
a_returnrate1 = float(input("Enter your expected annual retirement account return (typically .03-.07): "))
m_returnrate1 = (a_returnrate1 / 12)
y_retirein1 = int(input("Enter how many years you plan to be retired (typically 15 - 30): "))
m_retirein1 = (y_retirein1 * 12) #number of months till retirement

lumpsum1 = (m_withdraw*((1-(1+m_returnrate1)**(m_retirein1 * -1)) / m_returnrate1))

print("You will need ${0:,.2f} in your investment accounts to achieve this income".format (lumpsum1))

################################################################################################################################ Part 2

print()
y_retirein2 = int(input("How many years until you retire: "))
m_retirein2 = (y_retirein2 * 12)  #number of months till retirement
m_invest = int(input("What will your average monthly investment be: "))
a_returnrate2 = float(input("Enter your expected annual retirement account return (typically .03-.12): "))
m_returnrate2 = (a_returnrate2 / 12)

account_balance = m_invest * ((((1+m_returnrate2)** m_retirein2)-1)/m_returnrate2)
retirement_extra = (account_balance - lumpsum1) #determining the difference between the account balance and the lumpsup

print("Your retirement account will be worth ${0:,.2f}".format (account_balance))


if(account_balance >= lumpsum1): #maing sure to check if the amount of income is within the paramaters to be sufficent for the desired goal

   print("Congratulations you will achieve your income goal")

elif(account_balance < lumpsum1):

    print("You will need to save more money to reach your goal")

else:

    print("You will need to work longer to reach your goal")
##################################################################################################################################### Part 3

print()
question = str(input("Do you want to see the details: ")) #determin the input of if you want the results

if ((question == 'y') or ((question == 'Y') or (question == 'yes') or (question == 'Yes') or (question =='YES'))):  #check that the results were in line with wanting details provided
    print("For {0} years in retirement, you want ${1:,.2f} in monthly income with ${2:,.2f} coming from investments.".format (y_retirein2,m_income,m_withdraw))
    print("You saved ${0:,.2f} monthly for {1} years".format (m_invest,y_retirein2))

    if((account_balance > lumpsum1)):   #if paramaters were met then determin if account balance is larger or smaller and output accordingly

        print("This results in a retirement account balance surplus of ${0:,.2f}.".format (retirement_extra))

    if(account_balance < lumpsum1): #if paramaters were met then determin if account balance is larger or smaller and output accordingly

        print("This results in a retirement account balance deficit of ${0:,.2f}.".format (retirement_extra))
