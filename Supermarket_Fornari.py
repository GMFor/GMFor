#!/usr/bin/env python
# coding: utf-8

# # THE SUPERMAKET
# #### I have decided to keep my Python code in a single block to maintain a more homogeneous flow and an object-oriented approach. Additionally, consolidating the code in one block allows for easier management and understanding of the program's structure and facilitates code reuse. Moreover, it promotes modularity and encapsulation, enabling better organization and maintenance of the codebase over time. I was able to confirm these benefits by running the code.
# 
# ##### - The "Product" and "Customer" classes open the code, they handle specific information about products and customers respectively. This allows for more efficient and clear management of information related to each entity.
# 
# ##### - Then it follows the "Register_Manager" class handles operations related to the register of customers, such as reading files, adding new customers, modifying or deleting them, and saving changes to files. This structure allows for separating responsibilities and keeping inventory-related code focused within a single class.
# 
# ##### - Similarly, the "Inventory_Manager" class manages operations related to products
# 
# ##### - Then comes the  "Supermarket" class which coordinates operations between inventory and customer registry. It also handles sales, allowing customers to make purchases, updating inventory, and deducting the cost from the customer's balance. This class serves as the central point for interaction between other classes and supermarket operations.

# In[ ]:


class Product:
    def __init__(self, product_id, name, category, total_stock, price_per_unit):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.total_stock = total_stock
        self.price_per_unit = price_per_unit

    def modify(self, product_id, name, category, total_stock, price_per_unit):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.total_stock = total_stock
        self.price_per_unit = price_per_unit
        

#define path and file name 
inventory_file_name = "inventory_product_supermarket.txt"
inventory_file_path = "C:\\Users\\Giulia\\Desktop\\supermarket_files"



#similar to the class Product 
class Customer:
    def __init__(self, costumer_id, name, surname, address, account_balance):
        self.customer_id = costumer_id
        self.name = name
        self.surname = surname
        self.address = address
        self.account_balance = account_balance

    def modify(self, costumer_id, name, surname, address, account_balance):
        self.customer_id = costumer_id
        self.name = name
        self.surname = surname
        self.address = address
        self.account_balance = account_balance

#define path and file name
customers_file_name = "customers_supermarket.txt"
customers_file_path = "C:\\Users\\Giulia\\Desktop\\supermarket_files"



class Register_Manager:
    def __init__(self, customer_list = []):
        self.customer_list = customer_list

    def read_customers_file(self):  ## Function to read customer data from file
        self.customer_list = []
        try:
            f = open(customers_file_path + customers_file_name, "r")
        except Exception:
            f = open(customers_file_path + customers_file_name, "w")
            f.write("")
            f.close()
            f = open(customers_file_path + customers_file_name, "r")
        row = f.readline()  # Read the first row of the file
        while row:  # It enters a loop to read the file line by line until there are no more lines to read.
            if row:
                raw_customer = row.split(",")  # splits into a list of strings
                self.customer_list.append(Customer(raw_customer[0], raw_customer[1], raw_customer[2], raw_customer[3], float(raw_customer[4])))
                row = f.readline()
        f.close()

    def delete_customer(self): # # Remove the customer from the list and save the updated list
        customer_id = input("Insert customer Id to delete \n")
        # Retrieve the customer to modify
        customer_to_delete = None
        for customer in self.customer_list:
            if customer.customer_id == customer_id:
                customer_to_delete = customer
                break

        if customer_to_delete is None:
            print("No customer found for id:" + customer_id)
            return

        user_input =input("Once deleted the customer cannot be retrieved. Are you sure? Type \"yes\" to continue or \"no\" to cancel: ")
        if user_input == "no":
            return

        self.customer_list.remove(customer_to_delete)
        self.save_customers()
        print("Customer deleted!")

    def modify_customer(self): # Function to modify customer details
        customer_id = input("Insert customer Id to modify \n")
        # Retrieve the customer to modify
        customer_to_update_index = None
        for customer in self.customer_list:
            if customer.customer_id == customer_id:
                customer_to_update_index = self.customer_list.index(customer)
                break

        if customer_to_update_index is None:
            print("No customer found for id:" + customer_id)
            return

        print("Modifying customer.")
        name = input("- name: ")
        surname = input("- surname: ")
        address = input("- address: ")
        account_balance_raw = input("- account balance: ")
        if self._input_is_float(account_balance_raw):
            account_balance = float(account_balance_raw) #validation
        else:
            print("Account balance input was not a numeric value")
            return

        # Update customer details and save the updated list
        self.customer_list[customer_to_update_index].modify(customer_id, name, surname, address, account_balance)
        self.save_customers()
        print("Customer modified successfully!")

    def _input_is_float(self, input): #I have created this function to allow a validation: check if the input is a float
        try:
            float(input)
        except Exception:
            return False
        return True

    #add a new customer to the customer list
    def add_new_customer(self):
        print("Insert new customer information \n")
        customer_id = input("- customer id: ")
        name = input("- name: ")
        surname = input("- surname: ")
        address = input("- address: ")
        account_balance_raw = input("- account balance: ")
        if self._input_is_float(account_balance_raw):
            account_balance = float(account_balance_raw)#validation
        else:
            print("Account balance input was not a numeric value")
            return
        new_product = Customer(customer_id, name, surname, address, account_balance) #Create a new Customer object and append it to the customer list, so that it is updated
        self.customer_list.append(new_product)
        self.save_customers()
        print("Customer added successfully!")

        #display customer list
    def get_customer_list(self):
        print("There are "+str(len(self.customer_list))+" customers registred.\nCustomer ID, Name, Surname, Address, Account Balance\n")
        for customer in self.customer_list:
            print(customer.customer_id + "," + customer.name + "," + customer.surname + "," + customer.address + "," + str(customer.account_balance) + "\n")

    def save_customers(self): # Save customers to the customers file
        f = open(customers_file_path + customers_file_name, "w")  # To clean the file
        f.write("")
        f.close()

        f = open(customers_file_path + customers_file_name, "a") # Write each customer's details to the file
        for customer in self.customer_list:
            content = customer.customer_id + "," + customer.name + "," + customer.surname + "," + customer.address + "," + str(customer.account_balance)
            if self.customer_list.index(customer) == len(self.customer_list) - 1:
                content = content
            else:
                content = content + "\n"
            f.write(content)
        f.close()

    #function to start the register manager!
    def start(self):
        self.read_customers_file()
        while True:
            print("Select the operation you want to perform or type \"back\" and press enter: ")
            user_input = input("(1)Display the list of customers\n(2)Add a new customers \n(3)Modify customer\n(4)Delete customer\n")
            if user_input == "1":
                self.get_customer_list()
            elif user_input == "2":
                self.add_new_customer()
            elif user_input == "3":
                self.modify_customer()
            elif user_input == "4":
                self.delete_customer()
            elif user_input == "back":
                return
            else:
                print("Invalid operation input, select the operation you want to perform form the above elements")


                
                
#for the class Invenotry Manager the structure is similar as above               
                
class Inventory_Manager:
    def __init__(self, product_list = []):
        self.product_list = product_list

    def read_inventory_file(self):  # implemented to read the file
        self.product_list = []
        try:
            f = open(inventory_file_path + inventory_file_name, "r")
        except Exception:
            f = open(inventory_file_path + inventory_file_name, "w")
            f.write("")
            f.close()
            f = open(inventory_file_path + inventory_file_name, "r")
        row = f.readline()  # Read the first row of the file
        while row:  # It enters a loop to read the file line by line until there are no more lines to read.
            if row:
                raw_product = row.split(",")  # splits into a list of strings
                self.product_list.append(
                    Product(raw_product[0], raw_product[1], raw_product[2], int(raw_product[3]), float(raw_product[4])))
                row = f.readline()
        f.close()

        #display the list of products
    def get_product_list(self):
        print("There are "+str(len(self.product_list))+" products in the inventory.\nProduct ID, Name, Category, Total Stock, Price per Unit\n")
        for product in self.product_list:
            print (product.product_id+"," + product.name+","+product.category+","+ str(product.total_stock)+","+ str(product.price_per_unit)+"\n")

    def _input_is_int(self, input):  #check if input is an integer
        try:
            int(input)
        except Exception:
            return False
        return True

    def _input_is_float(self, input):  #check if input is a float 
        try:
            float(input)
        except Exception:
            return False
        return True

    #function to add new product
    def add_new_product(self):
        print("Insert new product information \n")
        product_id = input("- product id: ")
        name = input("- name: ")
        category = input("- category: ")
        total_stock_raw = input("- total stock: ")
        if self._input_is_int(total_stock_raw): #validation
            total_stock = int(total_stock_raw)
        else:
            print("Total stock input was not an integer")
            return
        price_per_unit_raw = input("- price per unit: ")
        if self._input_is_float(price_per_unit_raw):
            price_per_unit = float(price_per_unit_raw): #validation
        else:
            print("Price per unit input was not a numeric value")
            return
        # Create a new Product object and append it to the product list
        new_product = Product(product_id, name, category, total_stock, price_per_unit)
        self.product_list.append(new_product)
        self.save_products()
        print("Product added successfully!")

        #to modify a product 
    def modify_product(self):
        product_id = input("Insert product Id to modify \n")
        # Retrieve the product to modify
        product_to_update_index = None
        for product in self.product_list:
            if product.product_id == product_id:
                product_to_update_index = self.product_list.index(product)
                break

        print("Modifying product.")
        if product_to_update_index is None:
            print("No product found for id:" + product_id)
            return

        print("Modifying product")
        name = input("- name: ")
        category = input("- category: ")
        total_stock_raw = input("- total stock: ")
        if self._input_is_int(total_stock_raw):
            total_stock = int(total_stock_raw) # Validate if total stock input is an integer
        else:
            print("Total stock input was not an integer")
            return
        price_per_unit_raw = input("- price per unit: ")
        if self._input_is_float(price_per_unit_raw):
            price_per_unit = float(price_per_unit_raw) # Validate if price input is a float
        else:
            print("Price per unit input was not a numeric value")
            return
        self.product_list[product_to_update_index].modify(product_id, name, category, total_stock, price_per_unit)
        self.save_products()
        print("Product modified successfully!")

    def save_products(self): # Save product to the inventory file
        f = open(inventory_file_path + inventory_file_name, "w")  # To clean the file
        f.write("")
        f.close()

        f = open(inventory_file_path + inventory_file_name, "a")
        for product in self.product_list:
            content = product.product_id + "," + product.name + "," + product.category + "," + str(product.total_stock) + "," + str(product.price_per_unit)
            if self.product_list.index(product) == len(self.product_list) - 1:
                content = content
            else:
                content = content + "\n"
            f.write(content)
        f.close()

    ## Function to start the inventory manager!
    def start(self):
        self.read_inventory_file()
        while True:
            print("Select the operation you want to perform or type \"back\" and press enter: ")
            user_input = input("(1)Display the list of products\n(2)Add a new product to the inventory \n(3)Modify product\n")
            if user_input == "1":
                self.get_product_list()
            elif user_input == "2":
                self.add_new_product()
            elif user_input == "3":
                self.modify_product()
            elif user_input == "back":
                return
            else:
                print("Invalid operation input, select the operation you want to perform form the above elements")



class Supermarket:
    def __init__(self, inventory_manager, customer_manager):
        self.inventory_manager = inventory_manager
        self.customer_manager = customer_manager

    #function to perform a sale transaction
    def sale(self):
        #read inventory and customer data
        self.inventory_manager.read_inventory_file()
        self.customer_manager.read_customers_file()
        #request informations
        print("Insert the information request to complete the sale")
        customer_id = input("Id of customer that want to buy the product: ")
        product_id = input("Id of the product that the customer want to buy: ")
        quantity = int(input("Quantity of the product the user want to buy: "))

        # Initialize variables for product and customer
        product_to_buy = None
        product_to_buy_index = None
        costumer_buyer = None
        customer_buyer_index = None
        
        # Search for the product and customer in their respective lists
        for product in self.inventory_manager.product_list:
            if product.product_id == product_id:
                product_to_buy = product
                product_to_buy_index = self.inventory_manager.product_list.index(product)
        for customer in self.customer_manager.customer_list:
            if customer.customer_id == customer_id:
                costumer_buyer = customer
                customer_buyer_index = self.customer_manager.customer_list.index(customer)

        #validation based on real life scenarios 
        if product_to_buy is None:
            print("No product id found ")
            return
        if costumer_buyer is None:
            print("No costumer id found ")
            return
        if product_to_buy.total_stock == 0:
            print("No product in stock available")
            return
        if costumer_buyer.account_balance < product_to_buy.price_per_unit * quantity:
            print("Your balance is not enough")
            return
        if product_to_buy.total_stock < quantity:
            print("Not enough units available in stock")
            return

        # Update product stock and customer balance after the sale
        product_to_buy.total_stock = product_to_buy.total_stock - quantity
        costumer_buyer.account_balance = costumer_buyer.account_balance - product_to_buy.price_per_unit * quantity

        #modify customer and product information in their respective lists
        self.customer_manager.customer_list[customer_buyer_index].modify(costumer_buyer.customer_id, costumer_buyer.name, costumer_buyer.surname, costumer_buyer.address, costumer_buyer.account_balance)
        self.inventory_manager.product_list[product_to_buy_index].modify(product_to_buy.product_id, product_to_buy.name, product_to_buy.category, product_to_buy.total_stock, product_to_buy.price_per_unit)

        # Save updated customer and product data
        self.inventory_manager.save_products()
        self.customer_manager.save_customers()
        print("The customer " + costumer_buyer.name + " " + costumer_buyer.surname + " has purchased " + str(quantity) + " of " + product_to_buy.name + ".\nCustomer balance is now: " + str(costumer_buyer.account_balance))


    def insert_sample_data(self):
        # Add sample data to product file
        customers = [
            "2001,Alice,Marconi,123 Pine St,200.00\n",
            "2002,Bob,Williams,456 Oak St,150.00\n",
            "2003,Charlie,Smith,789 Elm St,0.00\n",
            "2004,David,Brown,101 Main St,250.00\n",
            "2005,Emma,Bianchi,246 Maple St,180.00\n",
            "2006,Frank,Davis,369 Birch St,0.00\n",
            "2007,Grace,Miller,4 Cedar St,270.00\n",
            "2008,Henry,Wilson,505 Pine St,320.00\n"
            "2009,Isabella,Turrini,50 Europe St,18.00"]
        f = open(customers_file_name + customers_file_path, "a")
        f.writelines(customers)
        f.close()

        # Add sample data to product file
        products = [
            "1001,Milk,Groceries,50,2.99\n",
            "1002,Toothpaste,Household,30,1.49\n",
            "1003,Bread,Groceries,40,1.99\n",
            "1004,Soap,Household,25,0.99\n",
            "1005,Apples,Fruits,60,3.49\n",
            "1006,Eggs,Groceries,70,2.49\n",
            "1007,Shampoo,Household,20,4.99\n",
            "1008,Bananas,Fruits,50,1.99\n",
            "1009,Rice,Groceries,45,3.99\n",
            "1010,Detergent,Household,45,4.99"
        ]
        f = open(inventory_file_path + inventory_file_name, "a")
        f.writelines(products)
        f.close()

    # Function to start the supermarket management system
    def start(self):
        while True:
            print("Select the operation you want to perform or type \"quit\" and press enter: ")
            user_input = input("(0) Add sample data to inventory and customer files \n(1) Inventory Management\n(2) Customer Management\n(3) Start sale \n")
            if user_input == "0":
                self.insert_sample_data()
                print("Sample data added correctly!")
            elif user_input == "1":
                self.inventory_manager.start()
            elif user_input == "2":
                self.customer_manager.start()
            elif user_input == "3":
                self.sale()
            elif user_input == "quit":
                return
            else:
                print("Invalid operation input, select the operation you want to perform form the above elements")


Supermarket(Inventory_Manager(), Register_Manager()).start()
 


# In[ ]:




