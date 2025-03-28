from abc import ABC, abstractmethod
from src.models.entities.pessoa_fisica import PessoaFisicaTable


class PessoaFisicaRepositoryInterface(ABC):
    @abstractmethod
    def insert_pessoa_fisica(
        self,
        renda_mensal: float,
        idade: int,
        nome_completo: str,
        celular: str,
        email: str,
        categoria: str,
        saldo: float,
    ) -> None:
        pass

    @abstractmethod
    def get_pessoa_fisica(self, pessoa_id: str) -> PessoaFisicaTable:
        pass
