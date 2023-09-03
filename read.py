def display_list():
    inventories =[]

    
    inventory_set={} # is a dictionary
    with open("inventories.txt","r") as file:
        for line in file:
            items, brand, price, unit =line.rstrip().split(",")
            inventory_set = {"items" :items, "brand": brand, "price": price, "unit": unit}
            inventories.append(inventory_set )
    print("List of Inventories".upper())
    print ("________________________________________________________________________________________________________")
    print("| {:<2}|  {:<35}|{:<25}|{:<20}|{:<11}|".format("S.N.", "Items", " Brand", " Price", " Unit"))
    for i,inventory in enumerate (inventories):
        print ("________________________________________________________________________________________________________")
        print("| {:<4}|  {:<35}|{:<25}|{:<20}|{:<11}|".format(i+1,inventory['items'].upper(), inventory['brand'].upper(), inventory['price'], inventory['unit']))
    print ("________________________________________________________________________________________________________")

def read_lines_of_inventories():
    inventory_list_size=[]
    with open("inventories.txt",'r') as file:
        size=1


        for line in file:
            
            line
            inventory_list_size.append(line.rstrip())
            size=size+1
    return size
    
    

def read_inventories():
    #with open, opens the file item.txt and 'r' read the file and store in variable 'file'
     with open("inventories.txt",'r') as file:
            #Creating an empty dictionary
            item_dictionary={} 
            item_id=1 
            #iterates every line in file
            for line_inFile in file: 
                #replacing empty line with spaces
                line_inFile=line_inFile.replace("\n",'') 
                #Using the comma as a seperator
                item_dictionary[item_id]=line_inFile.split(",") 
                item_id=item_id+1
            return item_dictionary
