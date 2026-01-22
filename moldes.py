from pydantic import BaseModel
import datetime
import random

# Modelos de dados para mensagens e classificações
class MensagemRecebida(BaseModel):
    texto: str
    remetente_id: int = random.randint(1000, 9999)
    horario: str = datetime.datetime.now().time()

# Modelo de resposta para classificação de mensagens
class ClassificacaoMensagem(BaseModel):
    categoria: str
