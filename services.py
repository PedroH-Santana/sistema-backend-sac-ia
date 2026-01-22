from dotenv import load_dotenv
from google import genai

load_dotenv()

# Inicializa o cliente GenAI
try:
    client = genai.Client()
except Exception as e:
    client = None

# Função para classificar mensagens usando o modelo Gemini
def classificar_mensagem(mensagem: str):
        if client == None:
            return "Erro ao conectar ao serviço de IA." 
        else:
            # Chama o modelo Gemini para classificar a mensagem
            try:
                response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=f"Você é um especialista em classficar mensagens, que atua na função de SAC. Você ira classficar as mensagens quanto a urgência na necessidade do cliente. As palavras chave para a classificação serão: 'Problema urgente', 'Problema comum', 'Pergunta nova/diferente', 'Dúvida comum', 'Elogio' e 'Reclamação leve'. Classifique a seguinte mensagem de acordo com essas categorias: '{mensagem}'. O formato de resposta deverá ser apenas a categoria.",
                )
                return response.text
            
            except Exception as e:
                return "Erro ao processar a mensagem."

