
#Rental Transactions
def write_transactions(transaction, transactions):
    # add the transactions to the database.txt file
    with open('database.txt', 'a') as f:
        for i, transaction in enumerate(transactions, 1):
            try:
                transaction_str = ', '.join(['{}:{}'.format(key, value) for key, value in transaction.items()])
                f.write('{}\n'.format(transaction_str))
            except AttributeError:
                print("Warning: Transaction {} is not a dictionary".format(i))




def write_return_transactions(transaction, transactions):
    # add the transactions to the database.txt file
    with open('returns_database.txt', 'a') as f:
        for i, transaction in enumerate(transactions, 1):
            try:
                transaction_str = ', '.join(['{}:{}'.format(key, value) for key, value in transaction.items()])
                f.write('{}\n'.format(transaction_str))
            except AttributeError:
                print("Warning: Transaction {} is not a dictionary".format(i))




def write_updated_inventories(inventories):
    with open('inventories.txt', 'w') as f:
        for inventory in inventories:
            f.write(', '.join(inventory) + '\n')

def print_invoice(invoice,filename):

    with open('database.txt', 'r') as file:
        # Create an empty dictionary to store the transactions grouped by invoice number
        transactions_by_invoice = {}
        # Iterate over the lines of the file
        for line in file:
            # Split the line into key-value pairs
            pairs = line.split(', ')
            # Create an empty dictionary to store the key-value pairs
            transaction = {}
            # Iterate over the key-value pairs
            #try:
            for pair in pairs:
                    # Split the pair into key and value
                key, value = pair.split(':')
                    # Strip any whitespace from the key and value
                key, value = key.strip(), value.strip()
            #except(ValueError):
                #print("Check database")
                # Add the key-value pair to the transaction dictionary
                transaction[key] = value
            # Check if the transaction has all the required keys
            if all(key in transaction for key in ['invoice', 'date', 'customer_name', 'phone_number', 'item_name', 'item_brand' ,'rental_period','item_price', 'unit']):
                # Get the values of the required keys
                invoice_no = transaction['invoice']
                date = transaction['date']

                
                customer_name = transaction['customer_name']
                phone_number = transaction['phone_number']
                item_name = transaction['item_name']
                item_brand = transaction['item_brand']
                rental_period =transaction['rental_period']
                item_price = transaction['item_price']
                unit = transaction['unit']
                
                
                if invoice_no == invoice:
                    # Add the transaction to the transactions_by_invoice dictionary
                    if invoice_no not in transactions_by_invoice:
                        transactions_by_invoice[invoice_no] = []
                    transactions_by_invoice[invoice_no].append(transaction)
        
        # Iterate over the transactions grouped by invoice number
        for invoice_no, transactions in transactions_by_invoice.items():
            if invoice_no == invoice:
                x = filename
                # Write the values to the invoice.txt file
                with open(x, "w") as f:
                    # Write the customer details and table headers to the file
                    f.write("\t\t\t\t\t\t\tSecret Shop\n")
                    f.write("\t\t\t\t\t\t\tPERFORMA INVOICE\n")
                    f.write("Name: " + customer_name + "\t\t\t\t\t\t\t\t\t\t\t" + "Date: " + date + "\n")
                    f.write("Phone Number: " + phone_number + "\t\t\t\t\t\t\t\t\t" + "Invoice: " + invoice_no + "\n")
                    f.write("Address: " + "Kathmandu, Nepal" + "\n")
                    f.write("________________________________________________________________________________________________________\n")
                    f.write("| {:<4}|  {:<35}|{:<25}|{:<20}|{:<11}|\n".format("S.N.", "Items", " Brand", " Unit", " Price"))
                    f.write("________________________________________________________________________________________________________\n")
                    total_price = 0
                    
                    for i, item in enumerate(transactions):
                        item_name = item['item_name']
                        item_brand = item['item_brand']
                        item_price = item['item_price']
                        unit = item['unit']
                        rental_period = item['rental_period']
                        
                        # Write the item to the file
                        f.write("| {:<4}|  {:<35}|{:<25}|{:<20}|{:<11}|\n".format(i+1, item_name, item_brand, unit, item_price))
                        total_price += int(item_price.strip("$")) * int(unit)
                    for i in range(20):
                        f.write("| {:<4}|  {:<35}|{:<25}|{:<20}|{:<11}|\n".format(" ", " ", "  ", "  ", ""))
                    f.write("________________________________________________________________________________________________________\n")
                    f.write("________________________________________________________________________________________________________\n")
                    f.write("Period of return \n")
                    f.write("| {:<4}|  {:<35}|{:<25}|{:<20}|{:<11}|\n".format(" ", "Rental Period", "  ", " " , str(rental_period)))
                    f.write("| {:<4}|  {:<35}|{:<25}|{:<20}|{:<11}|\n".format(" ", "Total Due Price: $", "  ", " " , str(total_price)))
                    f.write("________________________________________________________________________________________________________\n")
                    f.write("________________________________________________________________________________________________________\n")
    
        with open(filename, 'r') as f:
            invoice_contents = f.read()
            # Print the contents of the invoice file
            print(invoice_contents)
            """
    except FileNotFoundError:
        print('The file does not exist.')
        """
                        




def print_return_invoice(return_invoice):
    filename = return_invoice+"_R"+".txt"
    with open('returns_database.txt', 'r') as file:
    
        # Create an empty dictionary to store the transactions grouped by invoice number
        transactions_by_invoice = {}
        # Iterate over the lines of the file
        for line in file:
            # Split the line into key-value pairs
            pairs = line.split(', ')
            # Create an empty dictionary to store the key-value pairs
            transaction = {}
            # Iterate over the key-value pairs
            for pair in pairs:
                # Split the pair into key and value
                key, value = pair.split(':')
                # Strip any whitespace from the key and value
                key, value = key.strip(), value.strip()
                # Add the key-value pair to the transaction dictionary
                transaction[key] = value
            # Check if the transaction has all the required keys
            if all(key in transaction for key in ['invoice', 'return_date','rental_date', 'customer_name', 'phone_number', 'item_name', 'item_brand','rental_period', 'item_price', 'unit']):
                # Get the values of the required keys
                invoice_no = transaction['invoice']
                return_date = transaction['return_date']
                rental_date = transaction['rental_date']
                customer_name = transaction['customer_name']
                phone_number = transaction['phone_number']
                item_name = transaction['item_name']
                item_brand = transaction['item_brand']
                rental_period =transaction['rental_period']
                item_price = transaction['item_price']
                unit = transaction['unit']
                
                if invoice_no == return_invoice:
                    # Add the transaction to the transactions_by_invoice dictionary
                    if invoice_no not in transactions_by_invoice:
                        transactions_by_invoice[invoice_no] = []
                    transactions_by_invoice[invoice_no].append(transaction)
        
        # Iterate over the transactions grouped by invoice number
        for invoice_no, transactions in transactions_by_invoice.items():
            
            if invoice_no == return_invoice:
                # Write the values to the invoice.txt file
                
                with open(filename, "w") as f:
                    # Write the customer details and table headers to the file
                    f.write("\t\t\t\t\t\t\tSecret Shop\n")
                    f.write("\t\t\t\t\t\t\t INVOICE\n")
                    f.write("Name: " + customer_name + "\t\t\t\t\t\t\t\t\t\t\t" + "Date: " + return_date + "\n")
                    f.write("Phone Number: " + phone_number + "\t\t\t\t\t\t\t\t\t\t" + "Invoice: " + invoice_no + "\n")
                    f.write("Address: " + "Kathmandu, Nepal" + "\n")
                    f.write("________________________________________________________________________________________________________\n")
                    f.write("| {:<4}|  {:<35}|{:<25}|{:<20}|{:<11}|\n".format("S.N.", "Items", " Brand", " Unit", " Price"))
                    f.write("________________________________________________________________________________________________________\n")
                    total_price = 0
                    fine_amount =0
                    unit_fines=0
                    i=0
                    #fine per period = 10
                    for i in transactions_by_invoice:
                        
                        total_price += int(item_price.strip("$")) * int(unit)
                        fine_amount = date_check( rental_period, return_date, rental_date)
                        unit_fines +=int(unit)
                    #grand_total=total_price
                    grand_fine = fine_amount*unit_fines
                    grand_amount = total_price+grand_fine
                    
                    for i, item in enumerate(transactions):
                        item_name = item['item_name']
                        item_brand = item['item_brand']
                        item_price = item['item_price']
                        unit = item['unit']
                        
                        # Write the item to the file
                        f.write("| {:<4}|  {:<35}|{:<25}|{:<20}|{:<11}|\n".format(i+1, item_name, item_brand, unit, item_price))
                        
                        #Calculate Total Price
                        
                        #total_price += int(item_price.strip("$")) * int(unit) +int(result)
                    
                    for i in range(20):
                        f.write("| {:<4}|  {:<35}|{:<25}|{:<20}|{:<11}|\n".format(" ", " ", "  ", "  ", ""))
                    f.write("________________________________________________________________________________________________________\n")
                    f.write("| {:<4}|  {:<35}|{:<25}|{:<20}|{:<11}|\n".format(" ", "Total  Price: $", "  ", " " , str(total_price)))
                    f.write("________________________________________________________________________________________________________\n")
                    f.write("| {:<4}|  {:<35}|{:<25}|{:<20}|{:<11}|\n".format(" ", "Total Fine: $", "  ", " " , str(grand_fine)))
                    f.write("________________________________________________________________________________________________________\n")
                    f.write("| {:<4}|  {:<35}|{:<25}|{:<20}|{:<11}|\n".format(" ", "Grand Total: $", "  ", " " , str(grand_amount)))
                    
    try:
        with open(filename, 'r') as f:
            invoice_contents = f.read()
            # Print the contents of the invoice file
            print(invoice_contents)
    except FileNotFoundError:
        print("file not created")
        




def date_check( rental_period, return_date, rental_date):
    
            
    day1, month1, year1 = map(int, rental_date.split('-'))
    day2, month2, year2 = map(int, return_date.split('-'))

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

    date_difference= days
    
    if date_difference> (5*int(rental_period)):
        fine = ((days - int(rental_period)) // 5) * 10
    else:
        fine= 0
    
    return fine