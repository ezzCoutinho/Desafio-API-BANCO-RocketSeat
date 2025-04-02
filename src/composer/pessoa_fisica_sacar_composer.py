from src.controllers.pessoa_fisica_sacar_controller import (
    PessoaFisicaSacarController,
)
from src.models.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.models.settings.connection import db_connection_handler
from src.views.pessoa_fisica_sacar_view import PessoaFisicaSacarViews


def pessoa_fisica_sacar_composer() -> PessoaFisicaSacarViews:
    model = PessoaFisicaRepository(db_connection_handler)
    controller = PessoaFisicaSacarController(model)
    view = PessoaFisicaSacarViews(controller)
    return view
