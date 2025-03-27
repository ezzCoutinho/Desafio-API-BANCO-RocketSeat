from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.orm import sessionmaker


class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = "sqlite:///storage_init.db"
        self.__engine = None
        self.session = None

    def connect_to_db(self) -> None:
        self.__engine = create_engine(self.__connection_string)

    def get_engine(self) -> Engine:
        return self.__engine  # type: ignore

    def __enter__(self) -> "DBConnectionHandler":
        session_maker = sessionmaker()
        self.session = session_maker(bind=self.__engine)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if self.session:
            self.session.close()


db_connection_handler = DBConnectionHandler()
