import re
from typing import Dict

from src.controllers.interfaces.pessoa_juridica_creator_controller_interface import (
    PessoaJuridicaCreatorControllerInterface,
)
from src.errors.errors_types.http_bad_request import HttpBadRequest
from src.models.interfaces.pessoa_juridica_repository_interface import (
    PessoaJuridicaRepositoryInterface,
)


class PessoaJuridicaCreatorController(PessoaJuridicaCreatorControllerInterface):
    def __init__(
        self, pessoa_juridica_repository: PessoaJuridicaRepositoryInterface
    ) -> None:
        self.__pessoa_juridica_repository = pessoa_juridica_repository

    def create_pessoa_juridica(self, pessoa_juridica: Dict) -> Dict:
        faturamento = pessoa_juridica["faturamento"]
        idade = pessoa_juridica["idade"]
        nome_fantasia = pessoa_juridica["nome_fantasia"]
        celular = pessoa_juridica["celular"]
        email_corporativo = pessoa_juridica["email_corporativo"]
        categoria = pessoa_juridica["categoria"]
        saldo = pessoa_juridica["saldo"]

        self.__validate_nome_fantasia(nome_fantasia)
        self.__insert_pessoa_juridica(
            faturamento,
            idade,
            nome_fantasia,
            celular,
            email_corporativo,
            categoria,
            saldo,
        )

        formatted_response = self.__format_response(pessoa_juridica)

        return formatted_response

    def __validate_nome_fantasia(self, nome_fantasia: str) -> None:
        non_valid_characters = re.compile(r"[^a-zA-Z\s]")
        if non_valid_characters.search(nome_fantasia):
            raise HttpBadRequest("Nome fantasia inválido.")

    def __insert_pessoa_juridica(
        self,
        faturamento: float,
        idade: int,
        nome_fantasia: str,
        celular: str,
        email_corporativo: str,
        categoria: str,
        saldo: float,
    ) -> None:
        self.__pessoa_juridica_repository.insert_pessoa_juridica(
            faturamento,
            idade,
            nome_fantasia,
            celular,
            email_corporativo,
            categoria,
            saldo,
        )

    def __format_response(self, person_id: Dict) -> Dict:
        return {
            "data": {
                "type": "pessoa_juridica",
                "count": 1,
                "attributes": person_id,
            }
        }
