import pytest

from src.controllers.pessoa_fisica_sacar_controller import PessoaFisicaSacarController


class MockPessoaFisica:
    def __init__(self, id, saldo):
        self.id = id
        self.saldo = saldo


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

    def get_pessoa_fisica(self, pessoa_id: str):
        # Return a mock pessoa fisica object with the necessary attributes
        return MockPessoaFisica(id=pessoa_id, saldo=1000.00)


@pytest.mark.skip(reason="Teste OK")
def test_sacar_dinheiro_pessoa_fisica():
    pessoa_fisica = {
        "id": 1,
        "idade": 25,
        "nome_completo": "Joao Silva",
        "celular": "11999999999",
        "email": "teste@EMAIL.com",
        "categoria": "A",
        "saldo": 1000.00,
    }

    controller = PessoaFisicaSacarController(MockPessoaFisicaRepository())  # type: ignore
    response = controller.sacar_dinheiro_pessoa_fisica(pessoa_fisica["id"], 500.00)

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

    controller = PessoaFisicaSacarController(MockPessoaFisicaRepository())  # type: ignore

    with pytest.raises(Exception):
        controller.sacar_dinheiro_pessoa_fisica(pessoa_fisica["id"], 1500.00)
