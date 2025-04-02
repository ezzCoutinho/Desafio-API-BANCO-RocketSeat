from src.controllers.pessoa_juridica_creator_controller import (
    PessoaJuridicaCreatorController,
)
from src.models.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.models.settings.connection import db_connection_handler
from src.views.pessoa_juridica_creator_view import PessoaJuridicaCreatorView


def pessoa_fisica_creator_composer() -> PessoaJuridicaCreatorView:
    model = PessoaJuridicaRepository(db_connection_handler)
    controller = PessoaJuridicaCreatorController(model)
    view = PessoaJuridicaCreatorView(controller)
    return view
