class Customer():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, fullname, email, address):
        self.id = id
        self.fullname = fullname
        self.email = email
        self.address= address
