import json
def retrieve_json(filename):
    with open(filename,'r') as file:
        ret_data = dict(json.load(file))
        
    return ret_data

def append_dict_to_json(data, filename):
    with open(filename, 'r') as file:
        existing_data = dict(json.load(file))

    # Assuming the existing data is a list, you can append the new dictionary to it
    existing_data.update(data)



if __name__ == '__main__':
    filename = "client_details.json"
    filename1 = "employee_details.json"
    client_details = retrieve_json(filename)
    employee_detailsclient_details = {}
    client_email = input("ENTER THE EMAIL ID : ")
    client_password = input("ENTER A PASSWORD : ") 
    client_details[client_email] = client_password
    append_dict_to_json(client_details,filename)


    print(client_details)

    while True :
        client = input("ENTER THE EMAIL ID : ")
        if client in client_details.keys() :
            password = input("ENTER A PASSWORD : ")
            while True :
                if password == client_details[client] :
                    print("-------------------------------- HI WELCOME --------------------------------------- ")
                    print(" 1 - ORDERS ")
                    print(" 2 - VIEWING CUSTOMER DATABASE ")
                    break
                else :
                    print("INCORRECT PASSWORD")
                    password = input("ENTER A CORRECT PASSWORD : ")
            break

        else :
            print("INCORRECT EMAIL ID")
            client = input("ENTER THE EMAIL ID : ")

        
    n = int(input("HOW MANY EMPLOYEES : "))
    for i in range(n):
        employee_email = input("ENTER THE EMAIL ID : ")
        employee_password = input("ENTER A PASSWORD : ")
        employee_detailsclient_details[employee_email] = employee_password
        append_dict_to_json(employee_detailsclient_details,filename1)


    print(employee_detailsclient_details)


    while True :
        employee = input("ENTER THE EMAIL ID : ")
        if employee in employee_detailsclient_details.keys() :
            password = input("ENTER A PASSWORD : ")
            while True :
                if password == employee_detailsclient_details[employee] :
                    break
                else :
                    print("INCORRECT PASSWORD")
                    password = input("ENTER A CORRECT PASSWORD : ")
            break

        else :
            print("INCORRECT EMAIL ID")
            employee = input("ENTER THE EMAIL ID : ")

