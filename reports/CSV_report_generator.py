import openpyxl
import pathlib
import csv
from tkinter import messagebox
import pygame  # Importando pygame
from reports.generate_report import ReportGenerator

class CSVReportGenerator(ReportGenerator):
    def generate_report(self):
        try:
            ficheiro = pathlib.Path("Clientes.xlsx")

            if not ficheiro.exists():
                messagebox.showerror("Erro", "É necessário cadastrar ao menos 1 usuário")
                return

            workbook = openpyxl.load_workbook('Clientes.xlsx')
            folha = workbook.active

            with open('Relatório_de_Clientes.csv', mode='w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['Nome Completo', 'Contato', 'Idade'])

                for row in folha.iter_rows(min_row=2, values_only=True):
                    writer.writerow(row)

            # Reproduzindo o áudio de sucesso
            pygame.mixer.init()
            pygame.mixer.music.load('res/sounds/relatoriocsv.mp3')
            pygame.mixer.music.play()
            messagebox.showinfo("Sistema", "Relatório CSV gerado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao gerar o relatório: {e}")
