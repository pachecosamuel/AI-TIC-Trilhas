from langchain.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langgraph.graph import StateGraph, MessagesState
from langchain_core.runnables import Runnable
from dotenv import load_dotenv

# Carregar e preparar o PDF

loader = PyPDFLoader("aulam2a4/clima_brasil.pdf")
docs = loader.load()

# Concatenar o conteúdo

contexto = docs

# Definir a pergunta

pergunta = "Qual é o principal argumento do documento?"

# Template de prompt

template = """
Responda a pergunta abaixo com base no contexto fornecido. Se a pergunta não puder ser respondida com o contexto, diga que não sabe. Seja amigável e útil.:
{contexto}
{pergunta}

Answer:

"""
prompt = PromptTemplate(template=template, input_variables=["pergunta", "contexto"])
llm = ChatOpenAI(model="gpt-4o-mini")

# Criar cadeia de resposta

qna_chain = prompt | llm

# Definir grafo de execução

class State(dict):
   pergunta: str
   contexto: list
   resposta: str
graph_builder = StateGraph(State)

def generate(state: State):
   docs_content = "\n\n".join(doc.page(opens in a new tab)_content for doc in state["contexto"])
   response = qna_chain.invoke({"pergunta": state["pergunta"], "contexto": docs_content})
   return {"resposta": response.content}


graph_builder.add_node("generate", generate)
graph_builder.set_entry_point("generate")
graph_builder.set_finish_point("generate")
app = graph_builder.compile()

# Rodar o app com o contexto e pergunta

response = app.invoke({"contexto": contexto, "pergunta": pergunta})
print(response["resposta"])