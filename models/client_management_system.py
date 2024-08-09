from models.person import Person
import openpyxl
from openpyxl import Workbook
from tkinter import messagebox
import pathlib
import pygame
#sub classe de Person
class ClientManagementSystem(Person):
    def __init__(self, name="", contact="", age="", address=""):
        super().__init__(name, contact, age, address)
        self.__gender = "Masculino"  # Valor padrão
        self.__obs = ""

    # Getters
    def get_gender(self):
        return self.__gender

    def get_obs(self):
        return self.__obs

    # Setters
    def set_gender(self, gender):
        self.__gender = gender

    def set_obs(self, obs):
        self.__obs = obs

    def save_data(self):
        try:
            ficheiro = pathlib.Path("Clientes.xlsx")

            if not ficheiro.exists():
                ficheiro = Workbook()
                folha = ficheiro.active
                folha['A1'] = "Nome Completo"
                folha['B1'] = "Contato"
                folha['C1'] = "Idade"
                folha['D1'] = "Gênero"
                folha['E1'] = "Endereço"
                folha['F1'] = "Observações"
                ficheiro.save("Clientes.xlsx")

            ficheiro = openpyxl.load_workbook('Clientes.xlsx')
            folha = ficheiro.active
            folha.append([self.get_name(), self.get_contact(), self.get_age(), self.get_gender(), self.get_address(), self.get_obs()])
            ficheiro.save(r"Clientes.xlsx")
            pygame.mixer.init()
            pygame.mixer.music.load('res/sounds/dadossalvos.mp3')
            pygame.mixer.music.play()
            messagebox.showinfo("Sistema", "Dados salvos com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao salvar os dados: {e}")

    def clear_fields(self):
        self.set_name("")
        self.set_contact("")
        self.set_age("")
        self.set_address("")
        self.set_obs("")
