# pylint: disable=unused-argument
import pytest
from src.controllers.pessoa_juridica_get_controller import PessoaJuridicaGetController


class MockGetPessoaJuridica:
    def __init__(
        self,
        faturamento: float,
        idade: int,
        nome_fantasia: str,
        celular: str,
        email_corporativo: str,
        categoria: str,
        saldo: float,
    ) -> None:
        self.faturamento = faturamento
        self.idade = idade
        self.nome_fantasia = nome_fantasia
        self.celular = celular
        self.email_corporativo = email_corporativo
        self.categoria = categoria
        self.saldo = saldo


class MockPessoaJuridicaRepository:
    def get_pessoa_juridica(self, pessoa_id: str) -> MockGetPessoaJuridica:
        return MockGetPessoaJuridica(
            faturamento=1000,
            idade=20,
            nome_fantasia="João",
            celular="123456789",
            email_corporativo="alkjsdasjdlk@live.com",
            categoria="A",
            saldo=1000,
        )


@pytest.mark.skip(reason="Teste OK")
def test_get() -> None:
    controller = PessoaJuridicaGetController(MockPessoaJuridicaRepository())  # type: ignore
    response = controller.get_pessoa_juridica(pessoa_id="1")

    expected_response = {
        "data": {
            "type": "pessoa_juridica",
            "count": 1,
            "attributes": {
                "faturamento": 1000,
                "idade": 20,
                "nome_fantasia": "João",
                "celular": "123456789",
                "email_corporativo": "alkjsdasjdlk@live.com",
                "categoria": "A",
                "saldo": 1000,
            },
        }
    }

    assert response == expected_response
