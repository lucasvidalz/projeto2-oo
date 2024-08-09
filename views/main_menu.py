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
        self.geometry("700x500")  # Tamanho da janela configurado
        self.grid_rowconfigure(0, weight=1)  # Configura o layout da grid
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def create_widgets(self):
        # Título da aplicação
        lbl_title = ctk.CTkLabel(self, text="Sistema de Gestão de Clientes", font=("Helvetica", 24))
        lbl_title.grid(row=0, column=0, pady=20)

        # Descrição
        lbl_description = ctk.CTkLabel(self, text="Bem-vindo ao menu principal. Escolha uma das opções abaixo para continuar.", font=("Helvetica", 16))
        lbl_description.grid(row=1, column=0, pady=10)

        # Botão para ir para a tela de cadastro
        btn_go_to_register = ctk.CTkButton(self, text="Fazer Cadastro de Cliente", command=self.open_registration, fg_color="#151", hover_color="#131")
        btn_go_to_register.grid(row=2, column=0, pady=20)

        # Botão para gerar relatório
        btn_generate_report = ctk.CTkButton(self, text="Gerar Relatório de Todos os Clientes Cadastrados", command=self.generate_report, fg_color="#151", hover_color="#131")
        btn_generate_report.grid(row=3, column=0, pady=20)

        # Botão para fechar a aplicação
        btn_exit = ctk.CTkButton(self, text="Sair", command=self.quit, fg_color="#f55", hover_color="#d33")
        btn_exit.grid(row=4, column=0, pady=20)

    def open_registration(self):
        self.destroy()  # Fecha a tela inicial
        app = RegistrationForm()  # Abre a tela de cadastro
        app.mainloop()

    def generate_report(self):
        report_generator = ReportGenerator()
        report_generator.generate_report()