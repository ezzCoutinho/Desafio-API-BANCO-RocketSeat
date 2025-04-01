from flask import Blueprint, jsonify, request

from src.composer.pessoa_fisica_creator_composer import pessoa_fisica_creator_composer
from src.composer.pessoa_fisica_get_composer import pessoa_fisica_get_composer
from src.composer.pessoa_fisica_sacar_composer import pessoa_fisica_sacar_composer
from src.errors.errors_types.error_controller import handle_errors
from src.views.http_types.http_request import HttpRequest

pessoa_fisica_routes_bp = Blueprint("pessoa_fisica_routes", __name__)


@pessoa_fisica_routes_bp.route("/pessoa/fisica/creator", methods=["POST"])
def criar_pessoa_fisica():
    try:
        http_request = HttpRequest(body=request.json)  # type:ignore
        view = pessoa_fisica_creator_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        response = handle_errors(exception)
        return jsonify(response["body"]), response["status_code"]


@pessoa_fisica_routes_bp.route("/pessoa/fisica/get/<string:pessoa_id>", methods=["GET"])
def pegar_pessoa_fisica(pessoa_id: str):
    try:
        http_request = HttpRequest(param={"pessoa_id": pessoa_id})
        view = pessoa_fisica_get_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        response = handle_errors(exception)
        return jsonify(response["body"]), response["status_code"]


@pessoa_fisica_routes_bp.route(
    "/pessoa/fisica/sacar/<string:pessoa_id>", methods=["PATCH"]
)
def sacar_pessoa_fisica(pessoa_id: str):
    try:
        http_request = HttpRequest(param={"pessoa_id": pessoa_id}, body=request.json)  # type:ignore
        view = pessoa_fisica_sacar_composer()

        http_response = view.handle(http_request)
        return jsonify(http_response.body), http_response.status_code
    except Exception as exception:
        response = handle_errors(exception)
        return jsonify(response["body"]), response["status_code"]
