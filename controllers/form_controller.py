from tkinter import messagebox
from models.client_management_system import ClientManagementSystem

class FormController:
    def __init__(self):
        self.__client_system = ClientManagementSystem()

    def save_client(self, name, contact, age, address, gender, obs):
        if not name or not contact or not age:
            messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios.")
            return

        try:
            age = int(age)
            if age < 0:
                messagebox.showerror("Erro", "A idade não pode ser negativa.")
                return
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira uma idade válida.")
            return

        self.__client_system.set_name(name)
        self.__client_system.set_contact(contact)
        self.__client_system.set_age(age)
        self.__client_system.set_address(address)
        self.__client_system.set_gender(gender)
        self.__client_system.set_obs(obs)

        self.__client_system.save_data()
