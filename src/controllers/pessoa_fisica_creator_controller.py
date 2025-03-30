import re
from typing import Dict

from src.controllers.interfaces.pessoa_fisica_creator_controller_interface import (
    PessoaFisicaCreatorControllerInterface,
)
from src.errors.errors_types.http_bad_request import HttpBadRequest
from src.models.interfaces.pessoa_fisica_repository_interface import (
    PessoaFisicaRepositoryInterface,
)


class PessoaFisicaCreatorController(PessoaFisicaCreatorControllerInterface):
    def __init__(
        self, pessoa_fisica_respository: PessoaFisicaRepositoryInterface
    ) -> None:
        self.__pessoa_fisica_respository = pessoa_fisica_respository

    def create_pessoa_fisica(self, pessoa_fisica: Dict) -> Dict:
        renda_mensal = pessoa_fisica["renda_mensal"]
        idade = pessoa_fisica["idade"]
        nome_completo = pessoa_fisica["nome_completo"]
        celular = pessoa_fisica["celular"]
        email = pessoa_fisica["email"]
        categoria = pessoa_fisica["categoria"]
        saldo = pessoa_fisica["saldo"]

        self.__validate_nome_completo(nome_completo)
        self.__insert_pessoa_fisica(
            renda_mensal, idade, nome_completo, celular, email, categoria, saldo
        )

        formatted_response = self.__format_response(pessoa_fisica)

        return formatted_response

    def __validate_nome_completo(self, nome_completo: str) -> None:
        non_valid_characters = re.compile(r"[^a-zA-Z\s]")
        if non_valid_characters.search(nome_completo):
            raise HttpBadRequest("Nome da pessoa inválido.")

    def __insert_pessoa_fisica(
        self,
        renda_mensal: float,
        idade: int,
        nome_completo: str,
        celular: str,
        email: str,
        categoria: str,
        saldo: float,
    ) -> None:
        self.__pessoa_fisica_respository.insert_pessoa_fisica(
            renda_mensal, idade, nome_completo, celular, email, categoria, saldo
        )

    def __format_response(self, person_id: Dict) -> Dict:
        return {
            "data": {
                "type": "pessoa_fisica",
                "count": 1,
                "attributes": person_id,
            },
        }
