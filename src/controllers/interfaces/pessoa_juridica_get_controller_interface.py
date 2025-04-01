from typing import Dict
from abc import ABC, abstractmethod


class PessoaJuridicaGetControllerInterface(ABC):
    @abstractmethod
    def get_pessoa_juridica(self, pessoa_id: str) -> Dict:
        pass
