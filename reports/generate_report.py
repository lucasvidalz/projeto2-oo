# classe base
class ReportGenerator:
    # metodo polimorifico - vai ser usado para gerar diferentes tipos de arquivos
    def generate_report(self):
        raise NotImplementedError("Subclasses devem implementar este método.")
