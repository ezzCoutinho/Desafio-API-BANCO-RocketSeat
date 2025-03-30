from sqlalchemy import BIGINT, REAL, Column, String

from src.models.settings.base import Base


class PessoaJuridicaTable(Base):
    __tablename__ = "pessoa_juridica"

    id = Column(BIGINT, primary_key=True)
    faturamento = Column(REAL)
    idade = Column(BIGINT)
    nome_fantasia = Column(String)
    celular = Column(String)
    email_corporativo = Column(String)
    categoria = Column(String)
    saldo = Column(REAL)

    def __repr__(self) -> str:
        return (
            f"PessoaJuridica(id={self.id}, faturamento={self.faturamento}, "
            f"idade={self.idade}, nome_fantasia={self.nome_fantasia}, "
            f"celular={self.celular}, email_corporativo={self.email_corporativo}, "
        )
