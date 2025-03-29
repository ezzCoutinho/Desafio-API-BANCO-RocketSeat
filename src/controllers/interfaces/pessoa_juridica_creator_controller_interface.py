from typing import Dict
from abc import ABC, abstractmethod


class PessoaJuridicaCreatorControllerInterface(ABC):
    @abstractmethod
    def create_pessoa_juridica(self, pessoa_juridica: Dict) -> Dict:
        pass
