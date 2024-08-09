from tkinter import messagebox
from models.client_management_system import ClientManagementSystem
#classe de controle da entrada de dados, ela faz as verificações para a ClientManagement
class FormController:
    def __init__(self):
        self.client_system = ClientManagementSystem()

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

        self.client_system.set_name(name)
        self.client_system.set_contact(contact)
        self.client_system.set_age(age)
        self.client_system.set_address(address)
        self.client_system.set_gender(gender)
        self.client_system.set_obs(obs)

        self.client_system.save_data()
