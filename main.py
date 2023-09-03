from datetime import datetime
import sys
from write1 import  write_updated_inventories
import read
from operations import add_transactions, clear_inventories,inventories, return_transactions, add_inventories,date_calculator, latefees,valid_invoices
from write1 import  print_invoice, print_return_invoice
#from operation import date_calculator


"""rental function and rental_return has its own methods for executing day to day tranactions
a dictionaries are created where the rental and rental return transactions are stored
system_exit lets you exit the system
"""


def main():
    while True:
        read.display_list()
        user_input = input(" Enter 1 for Rentals\n Enter 2 for Rental Returns\n Enter 3 to exit\n => ")
        
        if user_input == "1":
            rental()

        elif user_input == "2":
            rental_return()

        elif user_input == "3":
            sys_exit()

        else:
            print("Please enter the valid command: (1-3)")
            

def rental():
    #Takes date self at each iteration.
    #rental_period = int(input("Enter the period of Rent"))
    date = date_calculator()
    inventory = read.read_inventories()
    lines_of_inventories_list= int(read.read_lines_of_inventories())
    
    #prompts user to enter the customer's details
    while True:
        try:
            customer_name = input("Name of the Customer: ")
            if len(customer_name) > 1 and customer_name.isalpha():
                break
            else:
                raise ValueError
        except ValueError:
            print("Please enter a valid name (more than 2 characters and only letters).")
    
    while True:
        try:
            phone_number = input("Phone Number: ")
            if not phone_number.isdigit() or len(phone_number) != 10:
                raise ValueError("Invalid phone number. Phone number must be 10 numeric digits.")
            break
        except ValueError as e:
            print(e)


    #Period of Rental (Multiples of 5)
    #Shop policy to rent in period
    
    
    while True:
        try:
            rental_period = int(input("Enter the period of Rent :"))
            if rental_period <= 0:
                raise ValueError("Period cannot be negative.\n Try Again!!!")
            break
        except ValueError as e:
            print(e)

    
    #Generates a unique identification number. Provides uniquesness to the invoice number
    invoice = customer_name + phone_number
    filename = invoice +".txt"
    

    
    #A list of inputs are created which stores the number of inventories rented by the user(administrator)


    while True:
        
        # Prompt the user to enter a product
        
        while True:
            try:
                product_number = input("Enter the Product Number: ")
                if not 1 <= int(product_number) <= lines_of_inventories_list:
                    raise ValueError("Invalid product number. Product number must be between 1 and 5.")
                break
            except ValueError as e:
                print(e)

    
        
        while True:
            try:
                unit = int(input("Enter no of units: "))
                if unit <= 0:
                    raise ValueError("Stock cannot be negative.\nEnter in Rental return")
                break
            except ValueError as e:
                print(e)


        
        selected_product =int (product_number)
        while (unit>int(inventories[selected_product][3]) or  int(inventories[selected_product][3])<=0):
            print("Sorry inventory doesn't exist")
            unit = int(input("Enter no of units: "))
        
        
        
            
        
        add_transactions(invoice,date, customer_name,phone_number,rental_period,product_number,unit)
        clear_inventories(product_number, unit)
       
        # Ask the user if they want to enter another product
        next_product = input("Enter another product? (Y/N): ").lower()
        if next_product == "y":
            continue
        elif next_product == "n":
            break
        else:
            print("Incorrect Input")
        
        

   
    # Call the write_updated_inventories() function from the write module
    write_updated_inventories(inventories)
    #print_invoice(unique_id, customer_name, date,phone_number, unit, product_number)
    print_invoice(invoice,filename)

    

    """ Local Variables and Global Variables: 
    Local Variables: variables defined within a function are only accessible within that function.
    Global Variables:variables with access to all functions.
    
    """



def rental_return():
    
        return_date  = date_calculator()
        #Rentals and rental return cannot be same date
        date_format = "%d-%m-%Y" # define the desired date format
        lines_of_inventories_list= int(read.read_lines_of_inventories())
        while True:
            try:
                rental_date = input("Enter Rental "+ date_format+": ")
                date = datetime.strptime(rental_date, date_format)
                break
            except ValueError:
                print("Invalid date format. Please try again.")


        #prompts user to enter the customer's details
        while True:
            try:
                customer_name = input("Name of the Customer: ")
                if len(customer_name) > 2 and customer_name.isalpha():
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Please enter a valid name (more than 2 characters and only letters).")


        while True:
            try:
                phone_number = input("Phone Number: ")
                if not phone_number.isdigit() or len(phone_number) != 10:
                    raise ValueError("Invalid phone number. Phone number must be 10 numeric digits.")
                break
            except ValueError as e:
                print(e)



        #Generates a unique identification number. Provides uniquesness to the invoice number

        returns_invoice = customer_name + phone_number
    
        #valid_invoices(returns_invoice)
        
        
            
        

        while True:
                try:
                    rental_period = int(input("Enter the period of Rent :"))
                    if rental_period <= 0:
                        raise ValueError("Period cannot be negative.\n Try Again!!!")
                    break
                except ValueError as e:
                    print(e)

    
    
    
        while True:
        # Prompt the user to enter a product
        
            while True:
                try:
                    product_number = input("Enter the Product Number: ")
                    if not 1 <= int(product_number) <= lines_of_inventories_list:
                        raise ValueError("Invalid product number. Product number must be between 1 and 5.")
                    break
                except ValueError as e:
                    print(e)
         #  product_number = input("Enter the Product Number: ")




            while True:
                try:
                    unit = int(input("Enter no of units: "))
                    if unit <= 0:
                        raise ValueError("Stock cannot be negative.\nEnter in Rental ")
                    break
                except ValueError as e:
                    print(e)


            return_transactions(returns_invoice,return_date, rental_date,customer_name,phone_number,rental_period,product_number,unit)
            add_inventories(product_number, unit)


            # Ask the user if they want to enter another product
            next_product = input("Enter another product? (Y/N): ").lower()
            if next_product == "y":
                continue
            elif next_product == "n":
                break
            else:
                print("Incorrect Input")

    # Call the write_updated_inventories() function from the write module
        write_updated_inventories(inventories)
    #print_invoice(unique_id, customer_name, date,phone_number, unit, product_number)
    
        print_return_invoice(returns_invoice)






def sys_exit():
    sys.exit(0)
main()