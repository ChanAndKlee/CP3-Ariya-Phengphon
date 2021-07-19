class Customer:
    # Attributes => Set as default
    name = ""
    age = 0
    gender = ""
    def addCart(self):
        print("Added "+self.name+" (",self.age,", "+self.gender+" )"+" successfully!")
# Create an object
customer1 = Customer()
customer1.name = "Chan"
customer1.age = 19
customer1.gender = "Female"

customer2 = Customer()
customer2.name = "Marco"
customer2.age = 30
customer2.gender = "Male"

customer3 = Customer()
customer3.name = "Lily"
customer3.age = 40
customer3.gender = "Female"

# print(customer1.addCart(), customer2.addCart(), customer3.addCart())
customer1.addCart()
customer2.addCart()
customer3.addCart()