from item import Item
from menu import _print_menu
import datetime
import pickle
import os

logs = []
items = []
id_count = 1
header = "this is a header"
items_file = "item.data"
logs_file = "logs.data"

def clear():
    return os.system("cls")


def get_time():
    curr_date = datetime.datetime.now()
    time = curr_date.strftime("%X")
    return time


def save_items():
    #open creates/open a file
    writer = open(items_file, "wb")
    pickle.dump(items, writer) #write binary (wb writes file) 
    writer.close() #closes the file(to release the file)
    print(" ** Saved: Data ** ")


def save_log():
    writer = open(logs_file, "wb")
    pickle.dump(logs, writer)
    writer.close()
    print(" ** Saved: Logs ** ") #saving acitivity logs rather than files


def read_items():
    global id_count
    #basically, this means: try to read the items, if not let me know
    try:
        reader = open(items_file, "rb") #rb = read file / read binary
        temp_list = pickle.load(reader) #transforms everything into objects

        for item in temp_list:
            items.append(item) #puts pickle.load stuff into container
        
        last = items[-1]
        id_count = last.id + 1 #adds id_count to elements last added in
        print(" Loaded: " + str(len(temp_list)) + "items") #show me it
    except:
        #you wind up here if the try crashes
        print("**** Error: Data could not be loaded ****")


#Functions : header_text, print_header, and print_all are added in by me, these are temps so that errors are not thrown.

def read_log():
    try:
        reader = open(logs_file, "rb") #rb = open file to Read Binary
        #rb convert it to the original object
        temp_list = pickle.load(reader)

        for log in temp_list:
            logs.append(log)
        
        print(" Loaded: " + str(len(temp_list)) + " log events")#show me
    
    except:
        #you get here if try block crashes
        print(" ** Error: Data could not be loaded! **")


def header_text():
    print("This is the Temporary Header Text line 13")


def print_header(text):
    print("\n\n")
    print("*" * 40)
    print(text)
    print("*" * 40)


def print_all(header_text):
    print_header(header_text)
    print("*" * 70)
    print("ID   | Item Title  | Category     | Price       | Stock")
    print("*" * 70)

    for item in items:
        print(str(item.id).ljust(3) + " | " + item.title.ljust(12) + " | " + item.category.ljust(12) + " | " + str(item.price).rjust(11) + " | " + str(item.stock).rjust(5))#the ljust/rjust show the length of the item


def register_item():
    global id_count

    print_header("Register New Item: ")
    title = input("Please input the title: ")
    category = input("Please input the category: ")
    price = float(input("Please input a price: "))
    stock = int(input("Please input the stock: "))

    #validations
    new_item = Item()
    new_item.id = id_count
    new_item.title = title
    new_item.category = category
    new_item.price = price
    new_item.stock = stock
    id_count += 1
    items.append(new_item)
    print(" Item Created!! ")


def update_stock():
    print_all("Update Stock")
    id = input("\n Select an ID to Update the Stock: ")
    found = False
    for item in items:
        if(str(item.id) == id):
            stock = input("please input new stock value: ")
            item.stock = int(stock)
            found = True

            #add registry to the log NOT NEEDED NOW, WILL ADD LATER
            # log_line = get_time() + " | Update |" + id
            # logs.append(log_line)
            # save_log()
    if(not found):
        print("** Error: ID doesn't exist, try again **")


def print_stock_value():
    total = 0.0
    for item in items:
        total += (item.price * float(item.stock))
    
    print("Total Stock Value: " + str(total))


def remove_items():
    print_all("Choose an Item to Remove ")
    id = input("\nSelect an ID to remove it: ")

    for item in items:
        if(str(item.id) == id):
            items.remove(item)
            print("Item has been removed")


def list_no_stock():
    print_header("Items With No Stock")
    for item in items:
        if(item.stock == 0):
            print(item.title)


def print_categories():
    temp_list = []

    for item in items:
        if(item.category not in temp_list):
            temp_list.append(item.category)
    print(temp_list)


def register_purchase():
    print_all("Choose an item that you purchased")
    id = input("\nSelect an ID to update its stock: ")

    found = False
    for item in items:
        if(str(item.id) == id):
            stock = input("How many Items? : ")
            item.stock += int(stock)
            found = True

    if(not found):
        print(" **Error: ID doesn't exist, recheck your inventory")


def register_sell():
    print_all("Choose an Item that you sold")
    id = input("\nSelect an ID to update its stock")

    found = False
    for item in items:
        if(str(item.id) == id):
            stock = input("How many Items? : ")
            item.stock -= int(stock)
            found = True
    
    if(not found):
        print(" **Error: ID doesn't exist, recheck your inventory")


# read previous data form the file to items array
read_items()


def read_log():
    
    for log in logs:
         log_line = get_time() + " | Update | " + id
         logs.append(log_line)
         print(log_line)

def print_log():
    read_log()



#meat and potatoes
option = ""
while(option != "x"):
    _print_menu()
    option = input("Select an option: ")
    if(option == "x"):
        break
    
    elif(option == '1'):
        register_item()
        save_items()
    elif(option == '2'):
        print_all(header_text)
        print(items)
        save_items()
    elif(option == '3'):
        stock_up = update_stock()
        print("Stock updated for: " + str(stock_up))
        save_items()
    elif(option == '4'):
        list_no_stock()
    elif(option == '5'):
        remove_items()
        save_items()
    elif(option == '6'):
        print_categories()
    elif(option == '7'):
        print_stock_value()
    elif(option == '8'):
        register_purchase()
    elif(option == '9'):
        register_sell()
    elif(option == '10'):
        print_log()

    if(option != "x"):
        input("\n\nPress Enter to coninue...")
