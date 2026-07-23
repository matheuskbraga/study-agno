from agno.agent import Agent
from agno.models.groq import Groq
from agno.tools.tavily import TavilyTools


# 1. Carregando as variáveis de ambiente
from dotenv import load_dotenv
load_dotenv()


# 2. Criando a função para calcular a temperatura em Fahrenheit
def celsius_to_fh(temperatura_celcius: float):
    """
    Converte a temperatura de Celsius para Fahrenheit.

    Args:
        temperatura_celcius (float): Temperatura em Celsius.

    Returns:
        float: Temperatura em Fahrenheit.
    """
    return (temperatura_celcius * 9/5) + 32


# 3. Criando o agente
agent = Agent(
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        TavilyTools(),
        celsius_to_fh, # 4. Passando a função criada para o agente
        ],
)


# 5. Resposta do agente com o poder da ferramenta.
agent.print_response(
    """
    Use suas ferramentas para pesquisar a temperatura hoje em Santa Maria, Rio Grande do Sul, em Fahrenheit.
    Retorne em um parágrafo simples e de fácil entendimento.
    """
)