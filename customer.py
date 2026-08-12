class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email


customer1 = Customer(1, "Yuni", "yuni@gmail.com")
customer2 = Customer(2, "Yeomin", "yeomin@gmail.com")
customer3 = Customer(3, "Trishna", "trishna@gmail.com")
customer4 = Customer(4, "Jisun", "jisun@gmail.com")

print(customer1.name)
print(customer2.name)
print(customer3.name)
print(customer4.name)

git config --global user.name "Yuni"
git config --global user.email "yunihan26@gmail.com"
git commit -m "Add customer data"
