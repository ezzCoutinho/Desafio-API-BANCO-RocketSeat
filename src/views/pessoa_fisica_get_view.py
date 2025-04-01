from src.controllers.interfaces.pessoa_fisica_get_controller_interface import (
    PessoaFisiscaGetControllerInterface,
)
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface


class PessoaFisicaGetView(ViewInterface):
    def __init__(self, controller: PessoaFisiscaGetControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        person_id = http_request.param["pessoa_id"]
        body_response = self.__controller.get_pessoa_fisica(person_id)

        return HttpResponse(status_code=201, body=body_response)
