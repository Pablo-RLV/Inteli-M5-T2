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

jogo = Jogos(Nome="DEAD SPACE REMAKE", Plataforma="PS5", Preco=350, Quantidade=10)
session.add(jogo)
session.commit()
jogo = Jogos(Nome="FORSPOKEN", Plataforma="PC", Preco=299, Quantidade=8)
session.add(jogo)
session.commit()
jogo = Jogos(Nome="DEAD ISLAND 2", Plataforma="PS5", Preco=250, Quantidade=10)
session.add(jogo)
session.commit()
jogo = Jogos(Nome="HOGWARTS LEGACY", Plataforma="PC", Preco=219, Quantidade=7)
session.add(jogo)
session.commit()
jogo = Jogos(Nome="WILD HEARTS", Plataforma="XBox Series", Preco=350, Quantidade=7)
session.add(jogo)
session.commit()
jogo = Jogos(Nome="RESIDENT EVIL 4", Plataforma="PS5", Preco=289, Quantidade=10)
session.add(jogo)
session.commit()
jogo = Jogos(Nome="THE LEGEND OF ZELDA: TEARS OF THE KINGDOM", Plataforma="Switch", Preco=350, Quantidade=10)
session.add(jogo)
session.commit()