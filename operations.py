

from write1 import write_transactions, write_return_transactions

def date_calculator():
    import datetime
    
    day = datetime.datetime.now().day
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    time_stamp = (str(day) +"-"+ str(month)+ "-"+ str(year)  ) 
    return time_stamp




#bringing inventories data into python file as a list
with open('inventories.txt', 'r') as f:
    inventories = [line.strip().split(', ') for line in f]
# Find the inventory with the matching product number
#Using properties of dictionary to assign values


def add_transactions(invoice,date, customer_name,phone_number,rental_period,product_number, unit):
    transactions=[]

    try:
        inventory = inventories[int(product_number) - 1]


        item_name, item_brand, item_price = inventory[0], inventory[1], inventory[2]
        """Transaction is entry
            Transactions is list, a collection of entries.
            We put Transaction in Transactions
        """

        transaction = {
        'invoice': invoice,
        'date':date,
        'customer_name': customer_name,
        'phone_number': phone_number,
        'product_number': product_number,
        'item_name': item_name,
        'item_brand': item_brand,
        'rental_period': rental_period,
        'item_price': item_price,
        'unit': unit}
        transactions.append(transaction)
        write_transactions(transaction, transactions)
    except(IndexError, UnboundLocalError, ValueError) as e:
        print("Wrong Product Number")
        
 

def clear_inventories(product_number, unit):
    inventory = inventories[int(product_number) - 1]
    item_unit = inventory[3]
    item_unit = str(int(item_unit) - int(unit))
    inventory[3] = item_unit
    
#rental_return

def return_transactions(invoice,return_date,rental_date, customer_name,phone_number,rental_period,product_number, unit):
    transactions=[]



    
    inventory = inventories[int(product_number) - 1]
    item_name, item_brand, item_price = inventory[0], inventory[1], inventory[2]
       
    transaction = {
    'invoice': invoice,
    'return_date':return_date,
    'rental_date': rental_date,
    'customer_name': customer_name,
    'phone_number': phone_number,
    'product_number': product_number,
    'item_name': item_name,
    'item_brand': item_brand,
    'rental_period':rental_period,
    'item_price': item_price,
    'unit': unit}
    transactions.append(transaction)
   
    write_return_transactions(transaction, transactions)
 

def clear_inventories(product_number, unit):
    try:
        inventory = inventories[int(product_number) - 1]
        item_unit = inventory[3]
        item_unit = str(int(item_unit) - int(unit))
        inventory[3] = item_unit
    except(IndexError, UnboundLocalError, ValueError) as e:
        print("Please enter product number from 1 to 5")


def add_inventories(product_number, unit):
    inventory = inventories[int(product_number) - 1]
    item_unit = inventory[3]
    item_unit = str(int(item_unit) + int(unit))
    inventory[3] = item_unit



def valid_invoices(returns_invoice):
    # Read the contents of the text files
    with open('database.txt', 'r') as f:
        lines = f.readlines()

    # Extract the relevant information from the text file
    databases = []
    for line in lines:
        database = {}
        for item in line.split(', '):
            key, value = item.split(':')
            database[key.strip()] = value.strip()
        databases.append(database)

    # Check if invoice_return is present in the database
    for database in databases:
        if returns_invoice == database['invoice']:
            print("Invoice "+returns_invoice+ " is  present in the database.")
            
        else:

            print("Invoice "+returns_invoice+ " is not present in the database.")




    
    
    
    """
    for database in databases:
        # Check if the invoice keys match
        if database['invoice'] != returns_database['invoice']:
            
            return False 
        else:
            print("Customer doesn't exists!!!!\n\n")
            return True # return False to indicate that the loop should stop
    """
            



def latefees():
    # Read the contents of the text files
    with open('database.txt', 'r') as f:
        lines = f.readlines()

    # Extract the relevant information from the text files
    databases = []
    for line in lines:
        database = {}
        for item in line.split(', '):
            key, value = item.split(':')
            database[key] = value
        databases.append(database)

    with open('returns_database.txt', 'r') as f:
        lines = f.readlines()

    # Extract the relevant information from the text files
    returns_databases = []
    for line in lines:
        returns_database = {}
        for item in line.split(', '):
            key, value = item.split(':')
            returns_database[key] = value
        returns_databases.append(returns_database)

        #returns_database = dict(item.split(':') for item in f.read().split(', '))

    # Process each database
    for database in databases:
        # Check if the invoice keys match
        if database['invoice'] == returns_database['invoice']:
            # Calculate the difference in date
            date1 = database['date'].split('-')
            date2 = returns_database['date'].split('-')
            date_diff = (int(date2[2]) - int(date1[2])) * 365 + (int(date2[1]) - int(date1[1])) * 30 + (int(date2[0]) - int(date1[0]))

            # Check if the difference in days exceeds 5

            if date_diff > 5:
                # Calculate the result
                item_price = float(database['item_price'].replace('$', ''))
                charging_days = date_diff -5
                unit = int(database['unit'])
                result = charging_days * (item_price/5)
                return charging_days,result
                
            else:
                print("The difference in days does not exceed 5.")
        else:
            print("Customer doesn't Exists!!!\n Create New Customer")
            







def date_check( rental, rental_return):
    from datetime import datetime
    date, rental_period= rental
    return_date = rental_return
    day1, month1, year1 = map(int, date.split('-'))
    day2, month2, year2 = map(int, return_date.split('-'))
    date_difference =return_date-date

    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Check for leap year
    if year1 % 4 == 0 and (year1 % 100 != 0 or year1 % 400 == 0):
        days_in_month[1] = 29

    # Calculate days between years
    if year2 - year1 ==1:
        days =0
    else:
        
        days = (year2 - year1) * 365

    # Add days for leap years
    for y in range(year1 + 1, year2):
        if y % 4 == 0 and (y % 100 != 0 or y % 400 == 0):
            days += 1

    # Calculate days between months
    if year2 > year1:
        for m in range(month1 - 1, len(days_in_month)):
            days += days_in_month[m]
        for m in range(0, month2 - 1):
            days += days_in_month[m]
    else:
        for m in range(month1 - 1, month2 - 1):
            days += days_in_month[m]

    # Calculate days between days
    if year2 > year1:
        days += day2 + (days_in_month[month1 - 1] - day1)
    else:
        days += day2 - day1
        
    
    if date_difference - (int(rental_period)*5) <=0:
        fine =0
        
    else:
        fine = ((days - int(rental_period)) // 5) * 10 #fine per period =10
    

    return fine
