from fastapi import FastAPI
from moldes import MensagemRecebida, ClassificacaoMensagem
from services import classificar_mensagem

app = FastAPI(
    title="Classificador de Mensagens SAC",
    description="API para a classificação de mensagens"
)

@app.post("/classificar", response_model=ClassificacaoMensagem)
def classificar(mensagem: MensagemRecebida):
    categoria = classificar_mensagem(mensagem.texto)
    return ClassificacaoMensagem(categoria=categoria)

