from pydantic import BaseModel, ValidationError, constr

from src.errors.errors_types.http_unprocessable_entity import HttpUnprocessableEntity
from src.views.http_types.http_request import HttpRequest


def pessoa_fisica_creator_validator(http_request: HttpRequest) -> None:
    class BodyData(BaseModel):
        renda_mensal: float
        idade: int
        nome_completo: constr(min_length=5)  # type: ignore
        celular: constr(min_length=5)  # type: ignore
        email: constr(min_length=5)  # type: ignore
        categoria: constr(min_length=5)  # type: ignore
        saldo: float

    try:
        BodyData(**http_request.body)
    except ValidationError as e:
        raise HttpUnprocessableEntity(e.errors()) from e
