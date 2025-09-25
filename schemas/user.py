from pydantic import BaseModel
from datetime import date
from typing import Optional

class EmpresaCreate(BaseModel):
    nome: str
    cnpj: str
    cidade: str
    ramo_atuacao: str
    telefone: str
    email_contato: str
    data_cadastro: date

class EmpresaUpdate(BaseModel):
    nome: Optional[str] = None
    cidade: Optional[str] = None
    ramo_atuacao: Optional[str] = None
    telefone: Optional[str] = None
    email_contato: Optional[str] = None
