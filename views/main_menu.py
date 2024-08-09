import customtkinter as ctk
from controllers.report_generator import ReportGenerator
from views.registration_form import RegistrationForm

class MainMenu(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.layout_config()
        self.create_widgets()

    def layout_config(self):
        self.title("Menu Principal")
        self.geometry("400x300")

    def create_widgets(self):
        # Botão para ir para a tela de cadastro
        btn_go_to_register = ctk.CTkButton(self, text="Fazer Cadastro de Cliente", command=self.open_registration, fg_color="#151", hover_color="#131")
        btn_go_to_register.pack(pady=50)

        # Botão para gerar relatório
        btn_generate_report = ctk.CTkButton(self, text="Gerar Relatório de Todos os Clientes Cadastrados", command=self.generate_report, fg_color="#151", hover_color="#131")
        btn_generate_report.pack(pady=50) # original pady = 20

    def open_registration(self):
        self.destroy()  # Fecha a tela inicial
        app = RegistrationForm()  # Abre a tela de cadastro
        app.mainloop()

    def generate_report(self):
        report_generator = ReportGenerator()
        report_generator.generate_report()
