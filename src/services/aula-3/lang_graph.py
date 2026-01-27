import os
import uuid
import getpass
from dotenv import load_dotenv
from langchain_cohere import ChatCohere
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

"""
LangChain separa três responsabilidades claras:

    Modelo (ChatCohere, ChatOpenAI, etc.)

    Prompt (ChatPromptTemplate)

    Execução (invoke())
"""

load_dotenv()

print("COHERE_API_KEY:", bool(os.getenv("COHERE_API_KEY")))
    

# Interagindo com a IA da Cohere
model = ChatCohere(
    model="command-a-03-2025",
    temperature=0.2
)

# Definir o grafo de estados para coordenar as mensagens
workflow = StateGraph(state_schema=MessagesState)

# Como chamar o modelo com mensagens
def call_model(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": response}

# Definir os estados da conversa
workflow.add_edge(START, "model")
workflow.add_node("model", call_model)

# Armazenamento da memória da conversa
memory = MemorySaver()
app = workflow.compile(checkpointer=memory)

# Definir o id da conversa pela thread
thread_id = uuid.uuid4()
config = {"configurable": {"thread_id": thread_id}}

query = "Olá, eu sou o Samuel!"

input_messages = [HumanMessage(query)]
output = app.invoke({"messages": input_messages}, config)
output["messages"][-1].pretty_print()

query = "Como eu me chamo?"

input_messages = [HumanMessage(query)]
output = app.invoke({"messages": input_messages}, config)
output["messages"][-1].pretty_print()

