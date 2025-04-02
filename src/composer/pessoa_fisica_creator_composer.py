from src.controllers.pessoa_fisica_creator_controller import (
    PessoaFisicaCreatorController,
)
from src.models.repositories.pessoa_fisica_repository import PessoaFisicaRepository
from src.models.settings.connection import db_connection_handler
from src.views.pessoa_fisica_creator_view import PessoaFisicaCreatorView


def pessoa_fisica_creator_composer() -> PessoaFisicaCreatorView:
    model = PessoaFisicaRepository(db_connection_handler)
    controller = PessoaFisicaCreatorController(model)
    view = PessoaFisicaCreatorView(controller)
    return view
