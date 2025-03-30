from typing import Dict
from abc import ABC, abstractmethod


class PessoaFisicaSacarControllerInterface(ABC):
    @abstractmethod
    def sacar_dinheiro_pessoa_fisica(self, pessoa_id: str, valor: float) -> Dict:
        pass
