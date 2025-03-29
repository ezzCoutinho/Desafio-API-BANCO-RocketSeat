class HttpBadRequest(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
        self.message = message
        self.name = "Bad Request"
        self.status_code = 400
