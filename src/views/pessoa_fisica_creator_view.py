from src.controllers.interfaces.pessoa_fisica_creator_controller_interface import (
    PessoaFisicaCreatorControllerInterface,
)
from src.validators.pessoa_fisica_creator_validator import (
    pessoa_fisica_creator_validator,
)
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface


class PessoaFisicaCreatorView(ViewInterface):
    def __init__(self, controller: PessoaFisicaCreatorControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        pessoa_fisica_creator_validator(http_request)

        person_info = http_request.body
        body_response = self.__controller.create_pessoa_fisica(person_info)

        return HttpResponse(status_code=201, body=body_response)
