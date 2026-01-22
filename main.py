from fastapi import FastAPI
from moldes import MensagemRecebida, ClassificacaoMensagem
from services import classificar_mensagem

#Configuração da API FastAPI
app = FastAPI(
    title="Classificador de Mensagens SAC",
    description="API para a classificação de mensagens"
)

# Endpoint GET para verificar se a API está funcionando
@app.get("/")
def read_root():
    return {"message": "Bem-vindo ao Classificador de Mensagens SAC"}

# Endpoint POST para classificar mensagens
@app.post("/classificar", response_model=ClassificacaoMensagem)
def classificar(mensagem: MensagemRecebida):
    categoria = classificar_mensagem(mensagem.texto)
    return ClassificacaoMensagem(categoria=categoria)


