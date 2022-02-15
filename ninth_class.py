from datetime import datetime
import random


data = {'3665935030': {'name': 'Desmond', 'dob': '31/21/21', 'bvn': '23456789', 'pin': '1234', 'bal': 185000}}

trans_data = {'3665935030': 
    [{'amount': 200000, 'type': 'credit', 'action': 'deposit', 'date': datetime.strptime('13-02-2022',"%d-%m-%Y").date()}, 
     {'amount': 12000, 'type': 'debit', 'action': 'withdrawal', 'date': datetime.strptime('14-02-2022',"%d-%m-%Y").date()},
     {'amount': 3000, 'type': 'debit', 'action': 'withdrawal', 'date': datetime.strptime('19-02-2022',"%d-%m-%Y").date()}]}

def get_stats(start_date:datetime, end_date:datetime, transactions:list):
    """_summary_
    Args:
        start_date (datetime): _description_
        end_date (datetime): _description_
        transactions (list): _description_
    """
    lower_limit = filter(lambda x:x['date']>=start_date, transactions)
    
    main_data = list(filter(lambda x:x['date']<=end_date, lower_limit))
    
    print(f"\nYour statement of account from {datetime.strftime(start_date, '%d-%b-%Y')} to {datetime.strftime(end_date, '%d-%b-%Y')} is given below:")
    for data in main_data:
        print(f"\nDate: {datetime.strftime(data['date'], '%d-%b-%Y')}")
        print(f"Amount: ${data['amount']}")
        print(f"Transaction Type: {data['type'].title()}")
        print(f"Action: {data['action'].title()}")
        
    #getting the average credits and debits
    credit = [data['amount'] for data in main_data if data['type']=='credit']
    debit = [data['amount'] for data in main_data if data['type']=='debit']
    
    try:
        average_credit = round(sum(credit)/len(credit), 3)
        print(f"The average credit during this period was ${average_credit}")
    except ZeroDivisionError:
        print("The average credit during this period was $0.00")
        
    try:
        average_debit = round(sum(debit)/len(debit),3)
        print(f"The average debit during this period was ${average_debit}")
    except ZeroDivisionError:
        print("The average debit during this period was $0.00")
    
    return 


print("Welcome to the AstroBank App")
while True:
    print("Enter s to signup or l to login:")
    print("Enter any other key to close")
    choice = input(">").lower()

    if choice == 'l':
        acc_num = input("Enter your account num:\n>")
        pin = input("Enter your pin:\n>")
        
        user = data.get(acc_num)
        
        if user and user['pin'] == pin:
            print(f"Welcome {user['name']}.\nYour account balance is ${user['bal']}")
            
            while True:
                print("""\nWhat would you like to do?
                    Press 1 to withdraw
                    Press 2 to deposit
                    Press 3 to transfer
                    Press 4 to get statement of account
                    Press any other key to quit.""")
                
                user_input = input(">")
                
                if user_input == '1':
                    amount = int(input("How much?\n>"))
                    if amount >= user['bal']:
                        print("Insufficient Funds")
                    else:
                        user['bal']-=amount
                        
                        #log transaction data
                        detail = {
                            "amount":amount,
                            "type": "debit",
                            "action" : "withdrawal",
                            "date" : datetime.now().date()
                            
                        }
                        
                        trans_data[acc_num].append(detail)
                        
                        
                        print("Please take your cash")
                        print(f"Balance is {user['bal']}")
                        
                elif user_input == '2':
                    amount = int(input("How much?\n>"))
                    
                    user['bal']+=amount
                    
                    #log transaction data
                    detail = {
                        "amount":amount,
                        "type": "credit",
                        "action" : "deposit",
                        "date" : datetime.now().date()
                    }
                    
                    trans_data[acc_num].append(detail)
                        
                    print("Successful")
                    print(f"Balance is {user['bal']}")
                elif user_input == '3':
                    recepient_ = input("Enter recepient account\n>")
                    amount = int(input("How much?\n>"))
                    
                    if user['bal'] < amount:
                        print("Insufficient Funds")
                    
                    recepient = data.get(recepient_)
                    if recepient:
                        recepient['bal'] += amount
                        user['bal'] -=amount
                        
                        #log transaction data
                        detail = {
                            "amount":amount,
                            "type": "debit",
                            "action" : "transfer",
                            "date" : datetime.now().date()
                        }
                        
                        trans_data[acc_num].append(detail)
                        
                        detail_recepient = {
                            "amount":amount,
                            "type": "credit",
                            "action" : "transfer",
                            "date" : datetime.now().date()
                        }
                        
                        trans_data[recepient_].append(detail_recepient)
                        
                        print("Successful")
                        print(f"Balance is {user['bal']}")
                    else:
                        print(f"Unable to fetch customer with account {recepient_}")
                elif user_input == '4':
                    
                    #get the start and end date. Using strptime method, convert the inputed string into datetime object.
                    start_date = datetime.strptime(input("Enter start date(dd-mm-yyyy)\n>"), "%d-%m-%Y").date()
                    end_date = datetime.strptime(input("Enter end date(dd-mm-yyyy)\n>"), "%d-%m-%Y").date()
                    #get the transaction from the trans_data dictionary
                    trans = trans_data[acc_num]
                    
                    # print(start_date)
                    # print(end_date)
                    # print(trans)
                    
                    get_stats(start_date, end_date, trans)
                          
                else:
                    print("Good bye")
                    break
        else:
            print("Invalid Login")
            
    elif choice == 's':
        name = input("Enter your name:\n>")
        dob= input("Enter your date of birth:\n>")
        bvn= input("Enter your BVN:\n>")
        pin = input("Enter your PIN:\n>")
        details = [('name', name), 
                ('dob', dob), 
                ('bvn', bvn), 
                ('pin', pin), 
                ('bal',0) 
                ]
    
        #generate account number
        num = [1,2,3,4,5,6,7,8,9,0]
        acc_num_list = ["3"]
        acc_num_list.extend([str(random.choice(num)) for _ in range(9)])
        
        
        acc_num = "".join(acc_num_list)
        
        data[acc_num] = dict(details)
        trans_data[acc_num] = []
        
        print(f"\nYour account has been created. You account number is {acc_num}\n")

    else:
        break



# print(data)
# print(trans_data)



#Functions#