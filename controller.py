from model import Usuario, get_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import hashlib

engine = get_engine()
Session = sessionmaker(bind=engine)
session = Session()

class ControllerCadastro:
    @classmethod
    def verifica_dados(cls, nome, email, senha):
        if len(nome) < 3:
            return 2
        if '@' not in email:
            return 3
        if len(senha) < 8:
            return 4
        
        return 1
    
    @classmethod
    def cadastrar(cls, nome, email, senha):
        usuario = session.query(Usuario).filter(Usuario.email == email).all()

        if len(usuario) > 0:
            return 5
        
        dados_verificados = cls.verifica_dados(nome, email, senha)

        if dados_verificados != 1:
            return dados_verificados
        try:
            senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()
            novoUsuario = Usuario(nome=nome, email=email, senha=senha)
            session.add(novoUsuario)
            session.commit()
            return 1
        except:
            return 6


class ControllerLogin:
    @classmethod
    def login(cls, email, senha):
        senha = hashlib.sha256(senha.encode('utf-8')).hexdigest()
        logado = session.query(Usuario).filter_by(email=email, senha=senha).all()

        if len(logado) == 1:
            return {'logado': True, 'id': logado[0].id}
        else:
            return False
