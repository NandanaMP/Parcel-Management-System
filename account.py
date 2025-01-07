import json
def login_or_create_account():
    while True:
        print("Welcome to the Parcel Delivery System!")
        print("1. Log in")
        print("2. Create an account")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            email = input("Enter your email: ")
            password = input("Enter your password: ")
            # Perform login validation
            if validate_login(email, password):
                print("Login successful!")
                # Proceed with the rest of the program
                break
            else:
                print("Invalid email or password. Please try again.")

        elif choice == "2":
            email = input("Enter an email-->: ")
            name = input("Enter your name-->")
            phoneno = int(input("Enter your phone number-->"))
            address = input("Enter your adress-->")
            # Check if the email already exists
            if email in customer_details:
                print("Email already exists. Please try again.")
                continue
            password = input("Enter a password: ")
            # Perform account creation
            create_account(email,name,address,phoneno,password)
            print("Account created successfully!")
            # Proceed with the rest of the program
            2

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

def validate_login(email, password):
    # Code to validate the login credentials
    # You can implement your own logic here, such as checking against a database or a file
    if email in customer_details and customer_details[email][0] == password:
        return True
    return False

def create_account(email,name,address,phoneno,password):
    # Code to create a new account
    # You can implement your own logic here, such as storing the customer details in a database or a file
    customer_details[email] = [password,name,address,phoneno]  # Assuming password is the only detail for now
    append_dict_to_json(customer_details, filename)


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

filename = "customer_details.json"
customer_details = retrieve_json(filename)  
login_or_create_account()