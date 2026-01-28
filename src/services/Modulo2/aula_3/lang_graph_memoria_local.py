# src\services\Modulo2\aula_3\lang_graph_memoria_local.py

import uuid
import sqlite3
from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage
from langgraph.checkpoint.sqlite import SqliteSaver
from langgraph.graph import StateGraph, START, MessagesState


# Modelo
model = ChatCohere(
    model="command-a-03-2025",
    temperature=0.2
)

# Definição do grafo
workflow = StateGraph(state_schema=MessagesState)


def call_model(state: MessagesState):
    response = model.invoke(state["messages"])
    return {"messages": response}


workflow.add_node("model", call_model)
workflow.add_edge(START, "model")


# Memória persistente local
conn = sqlite3.connect("memory.db", check_same_thread=False)
memory = SqliteSaver(conn)

app = workflow.compile(checkpointer=memory)


def chat(message: str, thread_id: str | None = None):

    # Normalização defensiva
    if thread_id in (None, "", "string", "null"):
        thread_id = None

    is_new_session = thread_id is None

    if is_new_session:
        thread_id = str(uuid.uuid4())

    config = {"configurable": {"thread_id": thread_id}}
    input_messages = [HumanMessage(message)]

    output = app.invoke({"messages": input_messages}, config)
    response = output["messages"][-1].content


    return {
        "new_session": is_new_session,
        "thread_id": thread_id,
        "response": response
    }