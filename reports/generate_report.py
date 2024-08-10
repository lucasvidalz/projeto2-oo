from abc import ABC, abstractmethod
# classe base
class ReportGenerator(ABC):
    # metodo polimorifico - vai ser usado para gerar diferentes tipos de arquivos
    @abstractmethod
    def generate_report(self):
        raise NotImplementedError("Subclasses devem implementar este método.")
