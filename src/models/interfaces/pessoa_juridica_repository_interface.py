from abc import ABC, abstractmethod

from src.models.entities.pessoa_juridica import PessoaJuridicaTable


class PessoaJuridicaRepositoryInterface(ABC):
    @abstractmethod
    def insert_pessoa_juridica(
        self,
        faturamento: float,
        idade: int,
        nome_fantasia: str,
        celular: str,
        email_corporativo: str,
        categoria: str,
        saldo: float,
    ) -> None:
        pass

    @abstractmethod
    def get_pessoa_juridica(self, pessoa_id: str) -> PessoaJuridicaTable:
        pass

    @abstractmethod
    def sacar_dinheiro_pessoa_juridica(
        self, pessoa_id: str, valor: float
    ) -> PessoaJuridicaTable:
        pass
