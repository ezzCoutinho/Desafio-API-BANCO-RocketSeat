class HttpUnprocessableEntity(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
        self.message = message
        self.name = "Unprocessable Entity"
        self.status_code = 422
