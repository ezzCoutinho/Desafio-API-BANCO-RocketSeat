import pytest
from src.controllers.pessoa_juridica_sacar_controller import (
    PessoaJuridicaSacarController,
)


class MockPessoaJuridica:
    def __init__(self, id, saldo):
        self.id = id
        self.saldo = saldo


class MockPessoaJuridicaRepository:
    def insert_pessoa_juridica(
        self,
        faturamento: str,
        idade: int,
        nome_fantasia: str,
        celular: str,
        email_corporativo: str,
        categoria: str,
        saldo: float,
    ) -> None:
        pass

    def get_pessoa_juridica(self, pessoa_id: str):
        # Return a mock pessoa fisica object with the necessary attributes
        return MockPessoaJuridica(id=pessoa_id, saldo=1000.00)


@pytest.mark.skip(reason="Teste OK")
def test_sacar_dinheiro_pessoa_fisica():
    pessoa_juridica = {
        "id": 1,
        "faturamento": 1,
        "idade": 25,
        "nome_fantasia": "Joao Silva",
        "celular": "11999999999",
        "email_corporativo": "teste@EMAIL.com",
        "categoria": "A",
        "saldo": 1000.00,
    }

    controller = PessoaJuridicaSacarController(MockPessoaJuridicaRepository())  # type: ignore
    response = controller.sacar_dinheiro_pessoa_juridica(pessoa_juridica["id"], 500.00)

    assert response["data"]["valor_sacado"] == 500.00


@pytest.mark.skip(reason="Teste OK")
def test_sacar_dinheiro_pessoa_fisica_error() -> None:
    pessoa_fisica = {
        "id": 1,
        "idade": 25,
        "nome_completo": "Joao Silva",
        "celular": "11999999999",
        "email": "teste@EMAIL.com",
        "categoria": "A",
        "saldo": 1000.00,
    }

    controller = PessoaJuridicaSacarController(MockPessoaJuridicaRepository())  # type: ignore

    with pytest.raises(Exception):
        controller.sacar_dinheiro_pessoa_juridica(pessoa_fisica["id"], 1500.00)
