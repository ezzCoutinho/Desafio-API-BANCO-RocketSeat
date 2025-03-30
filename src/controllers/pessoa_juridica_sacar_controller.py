from typing import Dict

from src.controllers.interfaces.pessoa_juridica_sacar_controller_interface import (
    PessoaJuridicaSacarControllerInterface,
)
from src.models.interfaces.pessoa_juridica_repository_interface import (
    PessoaJuridicaRepositoryInterface,
)


class PessoaJuridicaSacarController(PessoaJuridicaSacarControllerInterface):
    def __init__(
        self, pessoa_juridica_repository: PessoaJuridicaRepositoryInterface
    ) -> None:
        self.__pessoa_juridica_repository = pessoa_juridica_repository

    def sacar_dinheiro_pessoa_juridica(self, pessoa_id: str, valor: float) -> Dict:
        self.__validate_saque(pessoa_id, valor)
        formatted_response = self.__format_response(pessoa_id, valor)

        return formatted_response

    def __validate_saque(self, person_id: str, valor: float) -> None:
        if valor <= 0:
            raise ValueError("O valor do saque deve ser maior que zero.")

        pessoa = self.__pessoa_juridica_repository.get_pessoa_juridica(person_id)

        if not pessoa:
            raise ValueError("Pessoa física não encontrada.")

        limite_saque = pessoa.saldo * 0.8

        if valor > limite_saque:  # type: ignore
            raise ValueError(f"Valor excede o limite de saque de {limite_saque:.2f}.")

        if valor > pessoa.saldo:  # type: ignore
            raise ValueError("Saldo insuficiente para realizar o saque.")

    def __format_response(self, person_id: str, valor: float) -> Dict:
        pessoa = self.__pessoa_juridica_repository.get_pessoa_juridica(person_id)
        return {
            "sucess": True,
            "data": {
                "id": person_id,
                "valor_sacado": valor,
                "saldo_atual": pessoa.saldo,
                "mensagem": "Saque realizado com sucesso!",
            },
        }
