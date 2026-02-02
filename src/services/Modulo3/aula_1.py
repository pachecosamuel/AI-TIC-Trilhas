import streamlit as st
import os
import cohere
from dotenv import load_dotenv
from langchain_cohere import ChatCohere

load_dotenv()


# Título da aplicação
st.title("Chat com IA usando LangChain")

# Caixa de texto para o prompt
prompt = st.text_area("Digite sua pergunta:")

# Botão para enviar a pergunta
if st.button("Enviar"):
   if prompt:
       llm = ChatCohere(model="command-a-03-2025", temperature=0.9)

       resposta = llm.invoke(prompt)

       st.write("**Resposta:**", resposta.content)
   else:
       st.warning("Digite uma pergunta antes de enviar.")