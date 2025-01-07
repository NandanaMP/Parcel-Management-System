from datetime import date
from Queue import Queue
import random
import string
import json




idlist = []

def append_dict_to_json(data, filename):
    with open(filename, 'r') as file:
        existing_data = dict(json.load(file))

    # Assuming the existing data is a list, you can append the new dictionary to it
    existing_data.update(data)

    with open(filename, 'w') as file:
        json.dump(existing_data, file)

def retrieve_json(filename):
    with open(filename,'r') as file:
        ret_data = dict(json.load(file))
        
    return ret_data


def id_generator(cust,size=10):
    
    chars=string.ascii_uppercase + string.digits

    num = ''.join(random.choice(chars) for _ in range(size))
    idlist.append(num)
    while True:
        if num  not in idlist:
            order[num] = cust
            append_dict_to_json(order,filename)
            break
        else:
            num = ''.join(random.choice(chars) for _ in range(size))

    return order

class Order:
    def __init__(self,name,sender_address,rec_address,phone_no,item,ord_date):
        self.name = name
        self.sender_address = sender_address
        self.rec_address = rec_address
        self.phone_no = phone_no
        self.item = item
        self.ord_date = ord_date

    def display(self):

        return ""


def details():
    name = input("Enter your name")
    n = int(input("How many order do you want to add?"))
    send_address = input("Enter the sender address")  
    phone_no = int(input("Enter your phone number"))
    
    for i in range(n):

        rec_address = input("Enter the reciever address")
        priority = input("Does your order contain any important document (eg: Aadhar,pan card) y/n:")
        item = input("Enter item")
        today = date.today()
        ord_date = today.strftime("%B %d, %Y")

        #ord = Order(name,send_address,rec_address,phone_no,item,ord_date)
        #order_database.append(ord)
        '''Value as Order class'''
        #cust = ord
        '''Or value as list of details?'''
        cust = [name,send_address,item,rec_address,phone_no,ord_date]
        
        id_generator(cust)

    return ""


#Adding orders to the Queue
print()
print("Place your Order")
print()
filename = 'order_details.json'
order = retrieve_json(filename)
print(details())
pending_order = Queue()
'''Add orders to this queue if they are delivered'''
completed_order = Queue()

for id in order.keys():
    pending_order.enqueue(id)





