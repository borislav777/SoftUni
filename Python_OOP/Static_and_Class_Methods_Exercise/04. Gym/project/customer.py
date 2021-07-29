class Customer:
    ID = 0

    def __init__(self, name, address, email):
        Customer.ID += 1
        self.name = name
        self.address = address
        self.email = email
        self.id = Customer.ID

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"

    @staticmethod
    def get_next_id():
        return Customer.ID + 1
