import customtkinter as ctk
from tkinter import StringVar, END, messagebox

from models.client_management_system import ClientManagementSystem

class RegistrationForm(ctk.CTk, ClientManagementSystem):
    def __init__(self):
        ctk.CTk.__init__(self)
        ClientManagementSystem.__init__(self, name="", contact="", age="", address="")
        self.layout_config()
        self.appearence()
        self.todo_sistema()
        self.create_widgets()

        # atalhos de teclado ---
        self.bind('<Control-s>', self.save_shortcut)  # Atalho para salvar dados
        self.bind('<Control-l>', self.clear_shortcut)  # Atalho para limpar dados

    def layout_config(self):
        self.title("Sistema de Gestão de Clientes")
        self.geometry("700x500")

    def appearence(self):
        self.lb_apm = ctk.CTkLabel(self, text="Tema", bg_color="transparent", text_color=["#000", "#fff"])
        self.lb_apm.place(x=50, y=430)
        self.opt_apm = ctk.CTkOptionMenu(self, values=["System", "Dark", "Light"], command=self.change_apm)
        self.opt_apm.place(x=50, y=460)

    def create_widgets(self):
        # Text variables
        self.name_value = StringVar()
        self.contact_value = StringVar()
        self.age_value = StringVar()
        self.address_value = StringVar()

        # Entries
        self.name_entry = ctk.CTkEntry(self, width=350, textvariable=self.name_value, font=("Century Gothic bold", 16), fg_color="transparent")
        self.contact_entry = ctk.CTkEntry(self, width=200, textvariable=self.contact_value, font=("Century Gothic bold", 16), fg_color="transparent")
        self.age_entry = ctk.CTkEntry(self, width=150, textvariable=self.age_value, font=("Century Gothic bold", 16), fg_color="transparent")
        self.address_entry = ctk.CTkEntry(self, width=200, textvariable=self.address_value, font=("Century Gothic bold", 16), fg_color="transparent")

        # Combobox
        self.gender_combobox = ctk.CTkComboBox(self, values=["Masculino", "Feminino"], font=("Century Gothic bold", 14))
        self.gender_combobox.set("Masculino")

        # Textbox for observations
        self.obs_entry = ctk.CTkTextbox(self, width=470, height=150, font=("arial", 18), border_color="#aaa", border_width=2, fg_color="transparent")

        # Labels
        self.lb_name = ctk.CTkLabel(self, text="Nome Completo:", font=("Century Gothic bold", 16), text_color=["#000", "#fff"])
        self.lb_contact = ctk.CTkLabel(self, text="Contato:", font=("Century Gothic bold", 16), text_color=["#000", "#fff"])
        self.lb_age = ctk.CTkLabel(self, text="Idade:", font=("Century Gothic bold", 16), text_color=["#000", "#fff"])
        self.lb_gender = ctk.CTkLabel(self, text="Gênero:", font=("Century Gothic bold", 16), text_color=["#000", "#fff"])
        self.lb_address = ctk.CTkLabel(self, text="Endereço:", font=("Century Gothic bold", 16), text_color=["#000", "#fff"])
        self.lb_obs = ctk.CTkLabel(self, text="Observações:", font=("Century Gothic bold", 16), text_color=["#000", "#fff"])

        # Positioning elements in the window
        self.lb_name.place(x=50, y=120)
        self.name_entry.place(x=50, y=150)

        self.lb_contact.place(x=450, y=120)
        self.contact_entry.place(x=450, y=150)

        self.lb_age.place(x=300, y=190)
        self.age_entry.place(x=300, y=220)

        self.lb_gender.place(x=500, y=190)
        self.gender_combobox.place(x=500, y=220)

        self.lb_address.place(x=50, y=190)
        self.address_entry.place(x=50, y=220)

        self.lb_obs.place(x=50, y=260)
        self.obs_entry.place(x=180, y=260)

        # Buttons
        btn_submit = ctk.CTkButton(self, text="Salvar dados".upper(), command=self.submit, fg_color="#151", hover_color="#131")
        btn_submit.place(x=300, y=420)
        
        btn_clear = ctk.CTkButton(self, text="Limpar Campos".upper(), command=self.clear, fg_color="#555", hover_color="#333")
        btn_clear.place(x=500, y=420)
        
        # Botão Voltar
        btn_back = ctk.CTkButton(self, text="Voltar".upper(), command=self.back_to_main_menu, fg_color="#f55", hover_color="#c44")
        btn_back.place(x=50, y=420)  # Posicione conforme a sua necessidade

    def submit(self):
        if not self.name_value.get() or not self.contact_value.get() or not self.age_value.get():
            messagebox.showerror("Erro", "Por favor, preencha todos os campos obrigatórios.")
            return

        try:
            age = int(self.age_value.get())
            if age < 0:
                messagebox.showerror("Erro", "A idade não pode ser negativa.")
                return
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira uma idade válida.")
            return

        self.set_name(self.name_value.get())
        self.set_contact(self.contact_value.get())
        self.set_age(age)
        self.set_address(self.address_value.get())
        self.set_gender(self.gender_combobox.get())
        self.set_obs(self.obs_entry.get("1.0", END))

        self.save_data()

    def clear(self):
        self.clear_fields()
        self.name_entry.delete(0, END)
        self.contact_entry.delete(0, END)
        self.age_entry.delete(0, END)
        self.address_entry.delete(0, END)
        self.gender_combobox.set("Masculino")
        self.obs_entry.delete("1.0", END)

    def save_shortcut(self, event):  # Método acionado pelo atalho Ctrl+S
        self.submit()

    def clear_shortcut(self, event):  # Método acionado pelo atalho Ctrl+L
        self.clear()   

    def change_apm(self, theme):
        ctk.set_appearance_mode(theme)

    def todo_sistema(self):
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        
    def back_to_main_menu(self):
        self.withdraw()
        from views.main_menu import MainMenu  # Mover o import para dentro do método
        menu = MainMenu()
        menu.mainloop()
        self.destroy()