from typing import Dict
from abc import ABC, abstractmethod


class PessoaFisicaCreatorControllerInterface(ABC):
    @abstractmethod
    def create_pessoa_fisica(self, pessoa_fisica: Dict) -> Dict:
        pass
