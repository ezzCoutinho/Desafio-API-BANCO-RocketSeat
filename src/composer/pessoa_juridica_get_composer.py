from src.controllers.pessoa_juridica_get_controller import (
    PessoaJuridicaGetController,
)
from src.models.repositories.pessoa_juridica_repository import PessoaJuridicaRepository
from src.models.settings.connection import db_connection_handler
from src.views.pessoa_juridica_get_view import PessoaJuridicaGetView


def pessoa_fisica_get_composer() -> PessoaJuridicaGetView:
    model = PessoaJuridicaRepository(db_connection_handler)
    controller = PessoaJuridicaGetController(model)
    view = PessoaJuridicaGetView(controller)
    return view
