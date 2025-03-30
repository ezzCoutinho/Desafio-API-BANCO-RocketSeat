import pytest
from src.controllers.pessoa_juridica_creator_controller import (
    PessoaJuridicaCreatorController,
)


class MockPessoaJuridicaRepository:
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


@pytest.mark.skip(reason="Teste OK")
def test_create_pessoa_juridica() -> None:
    pessoa_juridica = {
        "faturamento": 1000.0,
        "idade": 30,
        "nome_fantasia": "Loja XYZ",
        "celular": "123456789",
        "email_corporativo": "asjkldaksj@Live.com",
        "categoria": "B",
        "saldo": 0.0,
    }

    controller = PessoaJuridicaCreatorController(
        MockPessoaJuridicaRepository()  # type: ignore
    )
    response = controller.create_pessoa_juridica(pessoa_juridica)

    assert response["data"]["type"] == "pessoa_juridica"
    assert response["data"]["count"] == 1
    assert response["data"]["attributes"] == pessoa_juridica


@pytest.mark.skip(reason="Teste OK")
def test_create_pessoa_fisica_error() -> None:
    pessoa_juridica = {
        "renda_mensal": "1250.00",
        "idade": 25,
        "nome_completo": "Joao 12Silva",
        "celular": "11999999999",
        "email": "teste@EMAIL.com",
        "categoria": "A",
        "saldo": 1000.00,
    }

    controller = PessoaJuridicaCreatorController(
        MockPessoaJuridicaRepository()  # type: ignore
    )

    with pytest.raises(Exception):
        controller.create_pessoa_juridica(pessoa_juridica)
