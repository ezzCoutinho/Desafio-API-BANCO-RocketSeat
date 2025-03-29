from sqlalchemy.exc import NoResultFound
from src.models.entities.pessoa_juridica import PessoaJuridicaTable
from src.models.interfaces.pessoa_juridica_repository_interface import (
    PessoaJuridicaRepositoryInterface,
)


class PessoaJuridicaRepository(PessoaJuridicaRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

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
        with self.__db_connection() as database:
            try:
                person_data = PessoaJuridicaTable(
                    faturamento=faturamento,
                    idade=idade,
                    nome_fantasia=nome_fantasia,
                    celular=celular,
                    email_corporativo=email_corporativo,
                    categoria=categoria,
                    saldo=saldo,
                )
                database.session.add(person_data)
                database.session.commit()
            except Exception as error:
                database.session.rollback()
                raise error

    def get_pessoa_juridica(self, pessoa_id: str) -> PessoaJuridicaTable:
        with self.__db_connection() as database:
            try:
                person = (
                    database.session.query(PessoaJuridicaTable)
                    .filter(PessoaJuridicaTable.id == pessoa_id)
                    .first()
                )
                return person
            except NoResultFound:
                return None  # type: ignore
