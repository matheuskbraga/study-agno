from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools


# 1. Carregando as variáveis de ambiente
from dotenv import load_dotenv
load_dotenv()


# 2. Criando o agente
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        TavilyTools(),
        ],
)


# 3. Resposta do agente
agent.print_response(
    """
    Use a ferramenta Tavily para pesquisar quais são os melhores
    investimentos para guardar um salário mensal no Brasil atualmente.
    Considere segurança, liquidez e rentabilidade. Retorne em um parágrafo simples e de fácil entendimento.
    """
)