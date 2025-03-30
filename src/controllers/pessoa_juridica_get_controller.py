from typing import Dict

from src.controllers.interfaces.pessoa_juridica_get_controller_interface import (
    PessoaFisicaGetControllerInterface,
)
from src.errors.errors_types.http_not_found import HttpNotFound
from src.models.entities.pessoa_juridica import PessoaJuridicaTable
from src.models.interfaces.pessoa_juridica_repository_interface import (
    PessoaJuridicaRepositoryInterface,
)


class PessoaFisicaGetController(PessoaFisicaGetControllerInterface):
    def __init__(
        self, pessoa_juridica_repository: PessoaJuridicaRepositoryInterface
    ) -> None:
        self.__pessoa_juridica_repository = pessoa_juridica_repository

    def get_pessoa_juridica(self, pessoa_id: str) -> Dict:
        person = self.__find_pessoa_juridica_in_db(pessoa_id)
        response = self.__format_response(person)

        return response

    def __find_pessoa_juridica_in_db(self, pessoa_juridica: str) -> PessoaJuridicaTable:
        person = self.__pessoa_juridica_repository.get_pessoa_juridica(pessoa_juridica)
        if not person:
            raise HttpNotFound("Pessoa não encontrada")

        return person

    def __format_response(self, person: PessoaJuridicaTable) -> Dict:
        return {
            "data": {
                "type": "pessoa_juridica",
                "count": 1,
                "attributes": {
                    "faturamento": person.faturamento,
                    "idade": person.idade,
                    "nome_fantasia": person.nome_fantasia,
                    "celular": person.celular,
                    "email_corporativo": person.email_corporativo,
                    "categoria": person.categoria,
                    "saldo": person.saldo,
                },
            }
        }
