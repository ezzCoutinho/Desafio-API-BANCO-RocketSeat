from src.controllers.interfaces.pessoa_juridica_creator_controller_interface import (
    PessoaJuridicaCreatorControllerInterface,
)
from src.validators.pessoa_juridica_creator_validator import (
    pessoa_juridica_creator_validator,
)
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface


class PessoaJuridicaCreatorView(ViewInterface):
    def __init__(self, controller: PessoaJuridicaCreatorControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pessoa_juridica_creator_validator(http_request)

        person_info = http_request.body
        body_response = self.__controller.create_pessoa_juridica(person_info)

        return HttpResponse(status_code=201, body=body_response)
