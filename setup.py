import os
from dotenv.main import load_dotenv
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.vectorstores import FAISS
from typing import Type, Dict
from pydantic import BaseModel, Field
from langchain.tools import BaseTool
from langchain.tools.retriever import create_retriever_tool
from langchain_experimental.agents.agent_toolkits import create_csv_agent
from langchain.agents import AgentExecutor, Tool, ZeroShotAgent
from langchain.chains import SimpleSequentialChain,StuffDocumentsChain, SequentialChain
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.prompts import (
    ChatPromptTemplate,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)
from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
from langchain.chains.router import MultiPromptChain
from langchain.chains import ConversationChain
from langchain.chains.router.llm_router import LLMRouterChain, RouterOutputParser
from langchain.chains.router.multi_prompt_prompt import MULTI_PROMPT_ROUTER_TEMPLATE

load_dotenv()

# initialize the llm
chat_llm = ChatOpenAI(api_key=os.environ['OPENAI_API_KEY'], model='gpt-4', temperature=0.34)

# load csv data
loader = CSVLoader(file_path='apartments.csv', encoding="utf-8", csv_args={
                'delimiter': ','})

data = loader.load()

embeddings = OpenAIEmbeddings(api_key=os.environ['OPENAI_API_KEY'])
vectorstore = FAISS.from_documents(data, embeddings)


instructions = """your are a realtor chat agent who sells apartments, your duty is to respond to purchase request for any of the apartment or house. 
                
                `if the user wants to make a purchase ask them for their: name, id_number and the apartment number`.
                
                `make sure that these values are passed if not keep persisting for them`.
                
                `if all the values are inputed, 
                
                << FORMATTING >>
                    Return a JSON object formatted to look like:
                    ```
                    {{
                        "name": string \ users name
                        "id_number": string \ users id_number
                        "apartment_id": string \ apartment id being purchased 
                    }}```


                """