# pylint: disable=unused-argument
import pytest

from src.controllers.pessoa_fisica_get_controller import PessoaFisicaGetController


class MockGetPessoaFisica:
    def __init__(
        self,
        renda_mensal: float,
        idade: int,
        nome_completo: str,
        celular: str,
        email: str,
        categoria: str,
        saldo: float,
    ) -> None:
        self.renda_mensal = renda_mensal
        self.idade = idade
        self.nome_completo = nome_completo
        self.celular = celular
        self.email = email
        self.categoria = categoria
        self.saldo = saldo


class MockPessoaFisicaRepositor:
    def get_pessoa_fisica(self, pessoa_id: str) -> MockGetPessoaFisica:
        return MockGetPessoaFisica(
            renda_mensal=1000,
            idade=20,
            nome_completo="João",
            celular="123456789",
            email="alkjsdasjdlk@live.com",
            categoria="A",
            saldo=1000,
        )


@pytest.mark.skip(reason="Teste OK")
def test_get() -> None:
    controller = PessoaFisicaGetController(MockPessoaFisicaRepositor())  # type: ignore
    response = controller.get_pessoa_fisica(pessoa_id="1")

    expected_response = {
        "data": {
            "type": "pessoa_fisica",
            "count": 1,
            "attributes": {
                "renda_mensal": 1000,
                "idade": 20,
                "nome_completo": "João",
                "celular": "123456789",
                "email": "alkjsdasjdlk@live.com",
                "categoria": "A",
                "saldo": 1000,
            },
        }
    }

    assert response == expected_response
