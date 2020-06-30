from tabulate import tabulate
from matplotlib import pyplot as plt
def menu():
    print('Enter 1 to start the main programe')
    print('Enter 2 to exit the programe')
    while True:
        try:
            user_choice = int(input('Please enter your choice: '))
            break
        except ValueError:
            print('That is not a correct value, please try again..')
    if int(user_choice) == int(1):
        main_programe()
    else:
        exit_programe()
            

def main_programe():
    print('This is a financial management programe')
    spend_fields = []
    i = True
    while i == True:
        fields=(input('Please enter what you spend your money on after you are done, enter "end": '))

        if fields == str('end'):
            i = False
        else:
            spend_fields.append(fields)
    print(spend_fields)

    expenditures = []
    for j in range(len(spend_fields)):
            expense = int(input('Please enter how much did you spend this month on '+str(spend_fields[j])+': '))
            expenditures.append(expense)
    print(expenditures)


    final_list = list(zip(spend_fields, expenditures)) # the zip function combines two lists into one 2d list
    print(final_list)


    for z in range (len(spend_fields)):
        print(spend_fields[z],' $',expenditures[z])

    total_outcome = sum(expenditures)
    print('This month your total money outcome was: '+str(total_outcome))




    headers = ['fields','money']
    print(tabulate(final_list, headers = headers, tablefmt='grid'))


    plt.axis('equal')
    plt.pie(expenditures, labels = spend_fields, autopct = '%0.2f%%')
    plt.title('Your expenditures')
    plt.show()
    
    money_income = int(input('Please enter your monthly income: '))
    net_cash_flow = money_income - total_outcome

    if net_cash_flow < 0:
        print('You might wanna slow down a bit. you re having a loss')
        print(net_cash_flow)
    else:
        print('Great you got $',str(net_cash_flow),' more')

    
    


def exit_programe():
    print('You have exitted the programe')

menu()

# An average person spends $550 on food / month
# An average perosn spends £66 to £137 / month on electricity
# An average person spends $161 on clothes / month
# An average person spends 
