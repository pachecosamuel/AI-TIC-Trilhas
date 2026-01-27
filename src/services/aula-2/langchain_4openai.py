import os
import getpass
import langchain
from langchain_cohere import ChatCohere
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage

"""
LangChain separa três responsabilidades claras:

    Modelo (ChatCohere, ChatOpenAI, etc.)

    Prompt (ChatPromptTemplate)

    Execução (invoke())
"""


if not os.environ.get("API_KEY"):
    os.environ["API_KEY"] = getpass.getpass("Enter API Key for OpenAI: ")
    

# 1° Forma de interagir via langchain - open ai
model = init_chat_model("gpt-4o-mini", model_provider="openai")

messages = [
    SystemMessage("Traduza o seguinte texto de inglês para português"),
    HumanMessage("Hello world!")
]

response = model.invoke(messages)
print(response.content)
# -----------------------------------------------------


# 2° Forma de interagir via langchain - open ai
system_template = "Traduza o seguinte texto de inglês para português"

prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("human", "{text}")]
)

prompt = prompt_template.invoke({"text": "Hello World"})

response = model.invoke(prompt)

print(response.content)