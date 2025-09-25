from fastapi import FastAPI, Depends, HTTPException
from schemas.user import EmpresaCreate, EmpresaUpdate
from config.db import Session
from model.user import EmpresaCliente

app = FastAPI()

def get_db ():
    db = Session()
    try:
        yield db
    finally:
        db.close()

# CREATE - Cadastro de empresa
@app.post("/empresas")
def create_empresa(empresa: EmpresaCreate, db: Session = Depends(get_db)):
    """
    Cria uma nova empresa no banco de dados.
    Retorna 400 se o CNPJ ou email já estiverem cadastrados.
    """

    db_empresa = EmpresaCliente(nome=empresa.nome, cnpj=empresa.cnpj, cidade=empresa.cidade, 
                                ramo_atuacao=empresa.ramo_atuacao, telefone=empresa.telefone, 
                                email_contato=empresa.email_contato, data_cadastro=empresa.data_cadastro)
    try:
        db.add(db_empresa)
        db.commit()
        db.refresh(db_empresa)
        return db_empresa
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="CNPJ ou email já cadastrado.")

# READ - Listagem de empresas com filtros e busca
@app.get("/empresas")
def get_empresas (db: Session = Depends(get_db), cidade: str | None = None, ramo_atuacao: str | None = None, nome: str | None = None):
    """
    Lista todas as empresas, permitindo filtros opcionais por cidade, ramo de atuação e busca por nome.
    """
    query = db.query(EmpresaCliente)
    if cidade:
        query = query.filter(EmpresaCliente.cidade.ilike(f"%{cidade}%"))
    if ramo_atuacao:
        query = query.filter(EmpresaCliente.ramo_atuacao.ilike(f"%{ramo_atuacao}%"))
    if nome:
        query = query.filter(EmpresaCliente.nome.ilike(f"%{nome}%"))
    return query.all()

# READ - Detalhes de uma empresa por ID
@app.get("/empresas/{empresa_id}")
def get_empresa_por_id(empresa_id: int, db: Session = Depends(get_db)):
    """
    Retorna os dados de uma empresa específica pelo ID.
    Retorna 404 se a empresa não existir.
    """
    db_empresa = db.query(EmpresaCliente).filter(EmpresaCliente.id == empresa_id).first()
    if (not db_empresa):
        raise HTTPException(status_code=404, detail="Empresa não encontrada.")
    return db_empresa

# UPDATE - Atualiza uma empresa
@app.put("/empresas/{empresa_id}")
def update_empresa(empresa_id: int, empresa_data: EmpresaUpdate,db: Session = Depends(get_db)):
    """
    Atualiza os campos de uma empresa existente.
    Retorna 404 se a empresa não existir ou 400 se houver conflito de CNPJ/email.
    """
    db_empresa = db.query(EmpresaCliente).filter(EmpresaCliente.id == empresa_id).first()
    if (not db_empresa):
        raise HTTPException(status_code=404, detail="Empresa não encontrada.")
    
    for (key, value) in empresa_data.dict(exclude_unset=True).items():
        setattr(db_empresa, key, value)

    try:
        db.commit()
        db.refresh(db_empresa)
        return db_empresa
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="CNPJ ou email já cadastrado.")

# DELETE - Exclusão de empresa
@app.delete("/empresas/{empresa_id}")
def delete_user(empresa_id: int, db: Session = Depends(get_db)):
    """
    Remove uma empresa do banco de dados pelo ID
    Retorna 404 se a empresa não existir.
    """
    db_empresa = db.query(EmpresaCliente).filter(EmpresaCliente.id == empresa_id).first()
    if (not db_empresa):
        raise HTTPException(status_code=404, detail="Empresa não encontrada.")
    
    db.delete(db_empresa)
    db.commit()
    return {"detail":"Empresa deletada com sucesso!"}