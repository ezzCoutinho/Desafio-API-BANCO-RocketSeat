from typing import Dict
from abc import ABC, abstractmethod


class PessoaFisiscaGetControllerInterface(ABC):
    @abstractmethod
    def get_pessoa_fisica(self, pessoa_id: str) -> Dict:
        pass
