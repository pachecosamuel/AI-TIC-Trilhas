import os
import getpass
from dotenv import load_dotenv
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

load_dotenv()

print("COHERE_API_KEY:", bool(os.getenv("COHERE_API_KEY")))
    

# Interagindo com a IA da Cohere
model = ChatCohere(
    model="command-a-03-2025",
    temperature=0.2
)

system_template = "Traduza o seguinte texto de inglês para {idioma}"

prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", system_template),
        ("human", "{text}")
    ]
)

prompt = prompt_template.invoke({
    "idioma": "Italian",
    "text": "Hello World!"
})

response = model.invoke(prompt)
print(response.content)