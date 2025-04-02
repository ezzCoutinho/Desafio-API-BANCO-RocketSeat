from src.controllers.pessoa_fisica_get_controller import (
    PessoaFisicaGetController,
)
from src.models.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.models.settings.connection import db_connection_handler
from src.views.pessoa_fisica_get_view import PessoaFisicaGetView


def pessoa_fisica_get_composer() -> PessoaFisicaGetView:
    model = PessoaFisicaRepository(db_connection_handler)
    controller = PessoaFisicaGetController(model)
    view = PessoaFisicaGetView(controller)
    return view
