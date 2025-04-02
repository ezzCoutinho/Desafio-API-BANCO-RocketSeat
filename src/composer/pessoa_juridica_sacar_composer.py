from src.controllers.pessoa_juridica_sacar_controller import (
    PessoaJuridicaSacarController,
)
from src.models.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.models.settings.connection import db_connection_handler
from src.views.pessoa_juridica_sacar_view import PessoaJuridicaSacarViews


def pessoa_fisica_sacar_composer() -> PessoaJuridicaSacarViews:
    model = PessoaJuridicaRepository(db_connection_handler)
    controller = PessoaJuridicaSacarController(model)
    view = PessoaJuridicaSacarViews(controller)
    return view
