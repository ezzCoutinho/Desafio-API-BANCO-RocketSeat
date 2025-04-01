import pytest

from src.controllers.pessoa_fisica_creator_controller import (
    PessoaFisicaCreatorController,
)


class MockPessoaFisicaRepository:
    def insert_pessoa_fisica(
        self,
        renda_mensal: str,
        idade: int,
        nome_completo: str,
        celular: str,
        email: str,
        categoria: str,
        saldo: float,
    ) -> None:
        pass


@pytest.mark.skip(reason="Teste OK")
def test_create_pessoa_fisica() -> None:
    pessoa_fisica = {
        "renda_mensal": 1250.00,
        "idade": 25,
        "nome_completo": "Joao Silva",
        "celular": "11999999999",
        "email": "teste@EMAIL.com",
        "categoria": "A",
        "saldo": 1000.00,
    }

    controller = PessoaFisicaCreatorController(
        MockPessoaFisicaRepository()  # type: ignore
    )
    response = controller.create_pessoa_fisica(pessoa_fisica)

    assert response["data"]["type"] == "pessoa_fisica"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == pessoa_fisica


@pytest.mark.skip(reason="Teste OK")
def test_create_pessoa_fisica_error() -> None:
    pessoa_fisica = {
        "renda_mensal": "1250.00",
        "idade": 25,
        "nome_completo": "Joao 12Silva",
        "celular": "11999999999",
        "email": "teste@EMAIL.com",
        "categoria": "A",
        "saldo": 1000.00,
    }

    controller = PessoaFisicaCreatorController(
        MockPessoaFisicaRepository()  # type: ignore
    )

    with pytest.raises(Exception):
        controller.create_pessoa_fisica(pessoa_fisica)
