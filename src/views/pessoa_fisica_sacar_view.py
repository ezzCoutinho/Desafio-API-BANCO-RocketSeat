from src.controllers.interfaces.pessoa_fisica_sacar_controller_interface import (
    PessoaFisicaSacarControllerInterface,
)
from src.views.http_types.http_request import HttpRequest
from src.views.http_types.http_response import HttpResponse
from src.views.interfaces.view_interface import ViewInterface


class PessoaFisicaSacarViews(ViewInterface):
    def __init__(self, controller: PessoaFisicaSacarControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        person_id = http_request.param["pessoa_id"]
        valor = float(http_request.body["valor"])
        body_response = self.__controller.sacar_dinheiro_pessoa_fisica(person_id, valor)

        return HttpResponse(status_code=200, body=body_response)
