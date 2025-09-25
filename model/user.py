from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import declarative_base
from config.db import engine

Base = declarative_base()

class EmpresaCliente(Base):
    __tablename__ = "empresas_clientes"

    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    cnpj = Column(String(25), unique=True)
    cidade = Column(String(50))
    ramo_atuacao = Column(String(50))
    telefone = Column(String(20))
    email_contato = Column(String(50), unique=True)
    data_cadastro = Column(Date)

Base.metadata.create_all(engine)