from typing import Dict

from src.controllers.interfaces.pessoa_juridica_sacar_controller_interface import (
    PessoaJuridicaSacarControllerInterface,
)
from src.errors.errors_types.http_bad_request import HttpBadRequest
from src.errors.errors_types.http_not_found import HttpNotFound
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
        saldo = self.__pessoa_juridica_repository.sacar_dinheiro_pessoa_juridica(
            pessoa_id, valor
        )

        formatted_response = self.__format_response(pessoa_id, valor, saldo)

        return formatted_response

    def __validate_saque(self, person_id: str, valor: float) -> None:
        if valor <= 0:
            raise HttpBadRequest("O valor do saque deve ser maior que zero.")

        pessoa = self.__pessoa_juridica_repository.get_pessoa_juridica(person_id)

        if not pessoa:
            raise HttpNotFound("Pessoa física não encontrada.")

        limite_saque = pessoa.saldo * 0.8

        if valor > limite_saque:  # type: ignore
            raise HttpBadRequest(
                f"Valor excede o limite de saque de {limite_saque:.2f}."
            )

        if valor > pessoa.saldo:  # type: ignore
            raise HttpBadRequest("Saldo insuficiente para realizar o saque.")

    def __format_response(self, pessoa_id: str, valor: float, saldo: float) -> Dict:
        return {
            "sucess": True,
            "data": {
                "id": pessoa_id,
                "valor_sacado": valor,
                "saldo_atual": saldo.saldo_atual  # type: ignore
                if hasattr(saldo, "saldo_atual")
                else saldo.saldo,  # type: ignore
                "mensagem": "Saque realizado com sucesso!",
            },
        }
