from sqlalchemy.exc import NoResultFound
from src.models.entities.pessoa_fisica import PessoaFisicaTable
from src.models.interfaces.pessoa_fisica_repository_interface import (
    PessoaFisicaRepositoryInterface,
)


class PessoaFisicaRepository(PessoaFisicaRepositoryInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

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
        with self.__db_connection() as database:
            try:
                person_data = PessoaFisicaTable(
                    renda_mensal=renda_mensal,
                    idade=idade,
                    nome_completo=nome_completo,
                    celular=celular,
                    email=email,
                    categoria=categoria,
                    saldo=saldo,
                )
                database.session.add(person_data)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    def get_pessoa_fisica(self, pessoa_id: str) -> PessoaFisicaTable:
        with self.__db_connection() as database:
            try:
                person = (
                    database.session.query(PessoaFisicaTable)
                    .filter(PessoaFisicaTable.id == pessoa_id)
                    .first()
                )
                return person
            except NoResultFound:
                return None  # type: ignore

    def sacar_pessoa_fisica(
        self,
        pessoa_id: str,
        valor: float,
    ) -> PessoaFisicaTable:
        with self.__db_connection() as database:
            try:
                person = (
                    database.session.query(PessoaFisicaTable)
                    .filter(PessoaFisicaTable.id == pessoa_id)
                    .first()
                )
                person.saldo -= valor
                database.session.commit()
                return person
            except Exception as exception:
                if isinstance(exception, NoResultFound):
                    raise NoResultFound("Pessoa não encontrada!")
                if person.saldo < valor:  # type: ignore
                    raise ValueError("Saldo insuficiente!")
                database.session.rollback()
                raise exception
