import openpyxl
import pathlib
from openpyxl import Workbook

class FileOperations:
    def create_client_file(self):
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

        except Exception as e:
            print(f"Ocorreu um erro ao criar o arquivo: {e}")
