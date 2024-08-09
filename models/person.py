class Person:
    def __init__(self, name, contact, age, address):
        self.__name = name
        self.__contact = contact
        self.__age = age
        self.__address = address

    # Getters
    def get_name(self):
        return self.__name

    def get_contact(self):
        return self.__contact

    def get_age(self):
        return self.__age

    def get_address(self):
        return self.__address

    # Setters
    def set_name(self, name):
        self.__name = name

    def set_contact(self, contact):
        self.__contact = contact

    def set_age(self, age):
        self.__age = age

    def set_address(self, address):
        self.__address = address
