from sqlalchemy import Column, String, BIGINT, REAL
from src.models.settings.base import Base


class PessoaFisica(Base):
    __tablename__ = "pessoa_fisica"

    id = Column(BIGINT, primary_key=True)
    renda_mensal = Column(REAL)
    idade = Column(BIGINT)
    nome_completo = Column(String)
    celular = Column(String)
    email = Column(String)
    categoria = Column(String)
    saldo = Column(REAL)

    def __repr__(self) -> str:
        return (
            f"PessoaFisica(id={self.id}, renda_mensal={self.renda_mensal}, "
            f"idade={self.idade}, nome_completo={self.nome_completo}, "
            f"celular={self.celular}, email={self.email}, "
            f"categoria={self.categoria}, saldo={self.saldo})"
        )
