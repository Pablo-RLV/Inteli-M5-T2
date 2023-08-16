from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///data.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Jogos(Base):
    __tablename__ = 'Jogos'
    Nome = Column(String, primary_key=True)
    Plataforma = Column(String)
    Preco = Column(Integer)
    Quantidade = Column(Integer)

Base.metadata.create_all(engine)

jogos_nome = session.query(Jogos.Nome).all()
jogos_plataforma = session.query(Jogos.Plataforma).all()
jogos_preco = session.query(Jogos.Preco).all()
jogos_quantidade = session.query(Jogos.Quantidade).all()
print(jogos_nome)
print(jogos_plataforma)
print(jogos_preco)
print(jogos_quantidade)