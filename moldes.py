from pydantic import BaseModel
import datetime
import random

class MensagemRecebida(BaseModel):
    texto: str
    remetente_id: int = random.randint(1000, 9999)
    horario: str = datetime.datetime.now().time()

class ClassificacaoMensagem(BaseModel):
    categoria: str