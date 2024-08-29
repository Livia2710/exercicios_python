# Importando ABC (Abstractb Base Classes) para criar Classe
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome):
        # Atributo privado (Encapsulado)
        self._nome = nome 

    # Metodo getter para acessar o atributo privado(Encapsulado)
    def get_nome(self):
        return self._nome

    # Método abstrato(Abstração)
    @abstractmethod
    def fazer_som(self):
        pass