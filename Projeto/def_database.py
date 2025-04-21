from sqlalchemy import create_engine, Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import sessionmaker,declarative_base

# criando banco de dados
db = create_engine('sqlite:///estoque.db')
Session = sessionmaker(bind=db)
session = Session()
Base = declarative_base()

class Produto(Base):
    __tablename__ = 'Produtos'
    id            = Column("id",Integer, primary_key=True, autoincrement=True)
    nome          = Column("Nome",String)
    quant         = Column("quant",Integer)
    precoVenda    = Column("precoVenda",Integer)
    precoCusto    = Column("precoCusto",Integer)

    def __init__(self, nome, quant, precoVenda, precoCusto):
        self.nome = nome
        self.quant = quant
        self.precoVenda = precoVenda
        self.precoCusto = precoCusto
    
    def Baixa(self, ValorBaixa):
        if ValorBaixa < 0:
            return "Erro: Valor de baixa inválido"
        elif self.quant == 0:
            return "Erro: Estoque vazio"
        elif self.quant - ValorBaixa < 0:
            return "Erro: Estoque insuficiente"
        else:
            self.quant -= ValorBaixa
            return f"Baixa realizada com sucesso. Estoque atual: {self.quant}"
    
    def Subir(self, ValorSubir):
        if ValorSubir < 0:
            return "Erro: Valor de subida inválido"
        else:
            self.quant += ValorSubir
            return f"Produto adicionado com sucesso. Estoque atual: {self.quant}"


Base.metadata.create_all(bind=db)