from typing import Dict

from src.controllers.interfaces.pessoa_fisica_get_controller_interface import (
    PessoaFisiscaGetControllerInterface,
)
from src.errors.errors_types.http_not_found import HttpNotFound
from src.models.entities.pessoa_fisica import PessoaFisicaTable
from src.models.interfaces.pessoa_fisica_repository_interface import (
    PessoaFisicaRepositoryInterface,
)


class PessoaFisicaGetController(PessoaFisiscaGetControllerInterface):
    def __init__(
        self, pessoa_fisica_repository: PessoaFisicaRepositoryInterface
    ) -> None:
        self.__pessoa_fisica_repository = pessoa_fisica_repository

    def get_pessoa_fisica(self, pessoa_id: str) -> Dict:
        person = self.__find_pessoa_fisica_in_db(pessoa_id)
        response = self.__format_response(person)

        return response

    def __find_pessoa_fisica_in_db(self, pessoa_fisica_id: str) -> PessoaFisicaTable:
        person = self.__pessoa_fisica_repository.get_pessoa_fisica(pessoa_fisica_id)
        if not person:
            raise HttpNotFound("Pessoa não encontrada")

        return person

    def __format_response(self, person: PessoaFisicaTable) -> Dict:
        return {
            "data": {
                "type": "pessoa_fisica",
                "count": 1,
                "atributes": {
                    "renda_mensal": person.renda_mensal,
                    "idade": person.idade,
                    "nome_completo": person.nome_completo,
                    "celular": person.celular,
                    "email": person.email,
                    "categoria": person.categoria,
                    "saldo": person.saldo,
                },
            }
        }
