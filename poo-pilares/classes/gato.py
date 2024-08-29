# Classe Gato herda de Animal tudo (Herança)
from classes.animal import Animal

class Gato(Animal):
    def __init__(self, nome, cor):
        # Chamando construtor da classe pai
        super().__init__(nome)
        self.cor = cor

#  Implementação do metodo do Poliformismo
    def fazer_som(self):
        return "Miau!"