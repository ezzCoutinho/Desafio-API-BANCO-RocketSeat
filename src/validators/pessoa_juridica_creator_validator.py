from pydantic import BaseModel, ValidationError, constr

from src.errors.errors_types.http_unprocessable_entity import HttpUnprocessableEntity
from src.views.http_types.http_request import HttpRequest


def pessoa_juridica_creator_validator(http_request: HttpRequest) -> None:
    class BodyData(BaseModel):
        faturamento: int
        idade: int
        nome_fantasia: constr(min_length=5)  # type: ignore
        celular: constr(min_length=5)  # type: ignore
        email_corporativo: constr(min_length=5)  # type: ignore
        categoria: constr(min_length=5)  # type: ignore
        saldo: float

    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntity(e.errors()) from e
