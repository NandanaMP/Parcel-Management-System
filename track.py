import random
import string

order = {}
numlist = []

def id_generator(cust,size=10):
    
    chars=string.ascii_uppercase + string.digits

    num = ''.join(random.choice(chars) for _ in range(size))
    numlist.append(num)
    while True:
        if num  not in numlist:
            order[num] = cust
            break
        else:
            num = ''.join(random.choice(chars) for _ in range(size))

    return order



def details():
    name = input("Enter your name")
    n = int(input("How many order do you want to plaqce?  "))
    send_add = input(" Sender address")
    
    phone = int(input("Enter your phone number"))
    


    for i in range(n):

        
        rec_add = input("Enter the reciever address")
        priority = input("Does you order comes under important documents (eg: Aadhar,Pan card....) ")

        # Add Priority Queue

        item = input("Enter item")
        cust = [name,send_add,item,rec_add,phone]
        
        print(id_generator(cust))

    return ''

print(details())




