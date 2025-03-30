from typing import Dict
from abc import ABC, abstractmethod


class PessoaJuridicaSacarControllerInterface(ABC):
    @abstractmethod
    def sacar_dinheiro_pessoa_juridica(self, pessoa_id: str, valor: float) -> Dict:
        pass
