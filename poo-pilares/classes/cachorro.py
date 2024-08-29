# Classe Cachoro herda de Animal tudo (Herança)
from classes.animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, raca):
        # Chamando construtor da classe pai
        super().__init__(nome)
        self.raca = raca

#  Implementação do metodo do Poliformismo
    def fazer_som(self):
        return "Au au!"