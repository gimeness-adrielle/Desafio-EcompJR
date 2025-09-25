from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="2427",
    host="127.0.0.1",
    database="crud_desafio",
    port="5432"
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)