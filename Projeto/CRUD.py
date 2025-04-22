from def_database import *


# for i in range(10):
#     item = Produto(nome=f'Produto {i}', quant=100, precoVenda=1000, precoCusto=200)
#     session.add(item)
#     session.commit()

# item = Produto(nome="Iphone", quant=100, precoVenda=5000, precoCusto=200)
# session.add(item)
# session.commit()


produto = session.query(Produto).filter_by(id=1).first()
produto.Baixa(1)
session.commit()