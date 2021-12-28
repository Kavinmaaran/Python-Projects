import mysql.connector as sql
#import json


def add_beneficiary():
    sq=sql.connect(host="localhost",user="root",passwd="kavin",database="money_management")
    #user_data_keys=["Name","Contact Number","ID"]
    user_pins={}
    user_id=int(input("Enter the Id:"))
    user_name=input("Enter the Username:")
    user_phone=input("Enter the Phone:")
    user_pin=int(input("Enter the pin(4 digits) :"))
    user_pins[user_id]=user_pin
    cursor=sq.cursor()
    cursor.execute("INSERT INTO `user_table` (`ID`, `Username`, `Phone`,`Pin`) VALUES ('{}', '{}', '{}','{}');".format(user_id,user_name,user_phone,user_pin))
    #cursor.execute(("SELECT `ID` FROM `user_table` WHERE `ID` != '{}'").format(user_id))
    #data=cursor.fetchall()
    #balance[user_id]={}
    #for i in data:
    #    balance[user_id][i]=0
    #print(balance)
    #json.dump(balance, open("balance_info.txt",'w'))
    sq.commit()
    sq.close()


def track_of_debts(id):
    sq=sql.connect(host="localhost",user="root",passwd="kavin",database="money_management")
    cursor=sq.cursor()
    print("Amount given to others:")
    cursor.execute(("SELECT * FROM `transaction` WHERE `Payer_id` = '{}' LIMIT 50").format(id))
    data=cursor.fetchall()
    for i in data:
        print(i[3])
    sq.commit()
    sq.close()    
    print("Amount taken from others:")
    sq=sql.connect(host="localhost",user="root",passwd="kavin",database="money_management")
    cursor=sq.cursor()
    cursor.execute(("SELECT * FROM `transaction` WHERE `receiver_id` = '{}' LIMIT 50").format(id))
    data=cursor.fetchall()
    for i in data:
        print(i[3])    
    sq.commit()
    sq.close()
    return 1


def transaction(payer_id):
    receive_id=int(input("Enter the id of the person whom you want to pay:"))
    pay_amount=int(input("Enter how much money you wish to pay:"))
    #balance[receive_id][payer_id]=-pay_amount
    #balance[payer_id][receive_id]=+pay_amount
    sq=sql.connect(host="localhost",user="root",passwd="kavin",database="money_management")
    cursor=sq.cursor()
    cursor.execute(("INSERT INTO `transaction` (`Payer_id`, `receiver_id`, `Amount`)VALUES ('{}', '{}', '{}');").format(payer_id,receive_id,pay_amount))
    sq.commit()
    sq.close()


def homepage():
    b=input("Do you want to create a new account(yes/no)")
    if(b=="no"):
        id=int(input("Enter the ID:"))
        pin=int(input("Enter your pin:"))
        sq=sql.connect(host="localhost",user="root",passwd="kavin",database="money_management")
        cursor=sq.cursor()
        cursor.execute(("SELECT `pin` FROM `user_table` WHERE `ID` = '{}'").format(id))
        epin=cursor.fetchall()
        sq.commit()
        sq.close()
        if (epin[0][0]==pin):  
            print('''
            1.Account Info
            2.Add Account
            3.Transaction
            4.Exit
            ''')
            a=int(input("Enter the option:"))
            while(a!=4):
                if(a==1):
                    track_of_debts(id)
                elif (a==2):
                    add_beneficiary()
                elif (a==3):
                    transaction(id)
                elif(a==4):
                    break           
                else :
                    print("Enter a valid number from the given options.")
                print("New action")
                print('''
                1.Account Info
                2.Add Account
                3.Transaction
                4.Exit
                ''')
                a=int(input("Enter the option:"))
        else:
            print("INVALID USER")
    elif (b=="yes"):
        add_beneficiary()
    else:
        print("SORRY TRY AGAIN")


"""try :
    balance = json.load(open("balance_info.txt"))
except:
    balance={}"""


print("MONEY MANAGEMENT")
sq=sql.connect(host="localhost",user="root",passwd="kavin",database="money_management")
cursor=sq.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS `user_table` (`ID` int NOT NULL,`Username` varchar(30) NOT NULL,`Phone` varchar(13) NOT NULL,`Pin` int(4) NOT NULL) ENGINE='InnoDB';")
cursor.execute("CREATE TABLE  IF  NOT EXISTS `transaction` (`Trans_ID` int NOT NULL AUTO_INCREMENT PRIMARY KEY,`Payer_id` int NOT NULL,`receiver_id` int NOT NULL,`Amount` int NOT NULL) ENGINE='InnoDB';")
sq.commit()
sq.close()

homepage()